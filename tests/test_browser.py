
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=640,480')

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.google.com")
    print("Заголовок:", driver.title)
finally:
    driver.quit()
    