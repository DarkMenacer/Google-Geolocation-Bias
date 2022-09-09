from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import time

def convert_b64 (value):
    value_bytes = value.encode("ascii")
    base64_bytes = base64.b64encode(value_bytes)
    return base64_bytes.decode("ascii")


PATH = Service("/usr/local/bin/geckodriver")

query = "restaurants"
city = "Pune,Maharashtra,India"
encoded_city = convert_b64(city)
key='W'

options = Options()
options.add_argument("--incognito")
driver = webdriver.Firefox(service=PATH)
driver.maximize_window()

final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQIC"+key+encoded_city
print(final_query)
driver.get('https://www.google.co.in/search?q=restaurants&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIWUHVuZSxNYWhhcmFzaHRyYSxJbmRpYQ==')

try:
    links = WebDriverWait(driver,10).until(
           EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.yuRUbf > a'))
        )
    for link in links:
        print(link.get_attribute("href"))
finally:
    driver.quit()
