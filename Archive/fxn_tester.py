from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep
import selenium



chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--window-size=1280,720")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--incognito')


def main(urls):

	url = urls[0]
	file = 'cnn.html'

	driver = uc.Chrome(version_main=107, options=chrome_options)
	driver.get(url)
	content = driver.page_source
	sleep(5)

	with open(file, 'w') as f: f.write(content);f.close()
	sleep(5)

	driver.quit()

	return



if __name__ == "__main__":

	urls = ["https://cnn.com/"]

	main(urls)