import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://selectorshub.com/xpath-practice-page/")
time.sleep(4)
links = driver.find_elements(By.TAG_NAME,('a'))
print(len(links))
for link in links:
    print(link.text)
