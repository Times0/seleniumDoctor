import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)


driver.get("https://www.python.org/")

time.sleep(5)

latest_version_element = driver.find_element(
    By.CSS_SELECTOR,
    "div.small-widget:nth-child(2) > p:nth-child(3) > a:nth-child(1)",
)
print(f"Latest Python version: {latest_version_element.text}")
driver.quit()
