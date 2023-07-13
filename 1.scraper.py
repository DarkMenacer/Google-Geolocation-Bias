from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import input.query_list as query_list
import input.city_list as city_list
import constants.consts_fxns as consts_fxns
import input.db_details
import psycopg2

def main():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    #chrome_options.add_argument("--window-size=1280,720")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--incognito')
    version = 111

    if input.db_details.CHROME_VERSION != 0:
        version = input.db_details.CHROME_VERSION

    driver = uc.Chrome(version_main=version, options=chrome_options)
    conn = psycopg2.connect(dbname=input.db_details.DB_NAME, user=input.db_details.DB_USER, password=input.db_details.DB_PASS, host=input.db_details.DB_HOST)
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS test_subjects (query TEXT, city TEXT, qcid SERIAL UNIQUE, PRIMARY KEY (query,city));")
        cur.execute("CREATE TABLE IF NOT EXISTS rbo_table (qcid BIGINT PRIMARY KEY, rbo NUMERIC(6,5), FOREIGN KEY (qcid) REFERENCES test_subjects(qcid));")
        cur.execute("CREATE TABLE IF NOT EXISTS links_table (qcid BIGINT PRIMARY KEY, links TEXT [], FOREIGN KEY (qcid) REFERENCES test_subjects(qcid));")
        cur.execute("TRUNCATE TABLE links_table, rbo_table, test_subjects RESTART IDENTITY CASCADE;")
        conn.commit()
        qcid = 1
        for query in query_list.queries:
            for city in city_list.cities:
                print("Scraping for " + query + " in " + city + ": ",end=" ")
                cur.execute("INSERT INTO test_subjects(query, city) VALUES (%s,%s);", (query,city))
                conn.commit()
                encoded_city = consts_fxns.convert_b64(city)
                key = consts_fxns.secret_keys[len(city)] 
                final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI"+key+encoded_city
                driver.get(final_query)
                print(final_query)

                link_elements = WebDriverWait(driver,20000).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.yuRUbf > a'))
                )

                ads = []
                try:
                    ads = WebDriverWait(driver,1).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.v5yQqb > a'))
                )
                    print("Ads were present")
                except:
                    print(end='')

                try:
                    peeps_also_ask = WebDriverWait(driver,1).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.tF2Cxc > .yuRUbf > a'))
                    )

                    # print("Peeps also ask is:"); consts_fxns.display(peeps_also_ask); print()
                    # print("All links are:"); consts_fxns.display(link_elements); print(); print()

                    if (len(peeps_also_ask) < 5):
                        link_elements = consts_fxns.adjust_links(link_elements,peeps_also_ask)
                    else:
                        peeps_also_ask1 = []
                        peeps_also_ask2 = []
                        i = 0
                        for link in peeps_also_ask:
                            if(i<4):
                                peeps_also_ask1.append(link)
                            else:
                                peeps_also_ask2.append(link)
                            i+=1
                        link_elements = consts_fxns.adjust_links(link_elements,peeps_also_ask1)
                        link_elements = consts_fxns.adjust_links(link_elements,peeps_also_ask2)
                
                except:
                    print("People Also Ask wasn't present")
                finally:
                    links = []

                    for element in ads:
                        links.append(str(element.get_attribute("href")))

                    for element in link_elements:
                        links.append(str(element.get_attribute("href")))
                    cur.execute("INSERT INTO links_table (qcid, links) VALUES (%s,%s);",(qcid,links))
                    conn.commit()
                    qcid+=1
                    driver.delete_all_cookies() #forcefully clearing cookies
    finally:
        driver.quit()
        cur.close()
        conn.close()
    return


if __name__ == "__main__":
    main()