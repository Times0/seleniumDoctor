from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

time.sleep(5)

latest_version_element = driver.find_element(
    By.CSS_SELECTOR,
    "div.small-widget:nth-child(2) > p:nth-child(3) > a:nth-child(1)",
)
print(f"Latest Python version: {latest_version_element.text}")
driver.quit()
