from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import query_list
import city_list
import consts_fxns
import psycopg2

PATH = Service("/usr/local/bin/geckodriver")
options = Options()
options.add_argument("--incognito")
driver = webdriver.Firefox(service=PATH, options=options)
driver.maximize_window()
conn = psycopg2.connect(dbname=consts_fxns.DB_NAME, user=consts_fxns.DB_USER, password=consts_fxns.DB_PASS, host=consts_fxns.DB_HOST)
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
            cur.execute("INSERT INTO test_subjects(query, city) VALUES (%s,%s);", (query,city))
            conn.commit()
            encoded_city = consts_fxns.convert_b64(city)
            key = consts_fxns.secret_keys[len(city)] 
            final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI"+key+encoded_city
            driver.get(final_query)
            link_elements = WebDriverWait(driver,20000).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.yuRUbf > a'))
                #EC.presence_of_all_elements_located((By.CSS_SELECTOR,'h3.LC20lb.MBeuO.DKV0Md'))
            )
            links = []
            for element in link_elements:
                #if(consts_fxns.find_in(element.get_attribute("href"), links) == 1):
                    links.append(element.get_attribute("href"))
                #if(element.text != ''):
                    #links.append(element.text)
            cur.execute("INSERT INTO links_table (qcid, links) VALUES (%s,%s);",(qcid,links))
            conn.commit()
            qcid+=1

finally:
    driver.quit()
    cur.close()
    conn.close()
