# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
with webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
) as driver:
    driver.get("https://python.org")
    print(driver.title)


### ___ Undetected Chromedriver ___ ###

import undetected_chromedriver as uc

with uc.Chrome() as driver:
    driver.get("https://python.org")
    print(driver.title)
