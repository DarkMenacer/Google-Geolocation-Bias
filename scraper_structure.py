from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import query_list
import city_list
import consts_fxns
from collections import defaultdict

di = defaultdict(list)

PATH = Service("/usr/local/bin/geckodriver")
options = Options()
options.add_argument("--incognito")
driver = webdriver.Firefox(service=PATH, options=options)
driver.maximize_window()

try:
    for query in query_list.queries:
        links_array = list()
        for city in city_list.cities:
            encoded_city = consts_fxns.convert_b64(city)
            key = consts_fxns.secret_keys[len(city)] 
            final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI"+key+encoded_city
            driver.get(final_query)
            links = WebDriverWait(driver,20000).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.yuRUbf > a'))
            )
            for link in links:
                links_array.append((city, link.get_attribute("href")))
        di[query] = links_array
    for query in di:
        print(query)
        for i in range(len(di[query])):
            print(di[query][i][0], di[query][i][1])
finally:
    driver.quit()
