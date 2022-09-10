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

try:
    conn = psycopg2.connect(dbname=consts_fxns.DB_NAME, user=consts_fxns.DB_USER, password=consts_fxns.DB_PASS, host=consts_fxns.DB_HOST)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scraped_links (id SERIAL PRIMARY KEY, city VARCHAR(50),query TEXT, link TEXT);")
    conn.commit()
    for query in query_list.queries:
        for city in city_list.cities:
            encoded_city = consts_fxns.convert_b64(city)
            key = consts_fxns.secret_keys[len(city)] 
            final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI"+key+encoded_city
            driver.get(final_query)
            links = WebDriverWait(driver,20000).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.yuRUbf > a'))
            )
            for link in links:
                cur.execute("INSERT INTO scraped_links(city, query, link) VALUES (%s,%s,%s)",(city,query,link.get_attribute("href")))
                conn.commit()
finally:
    cur.close()
    conn.close()
    driver.quit()
