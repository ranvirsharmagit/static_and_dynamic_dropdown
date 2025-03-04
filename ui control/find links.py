import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://selectorshub.com/xpath-practice-page/")
time.sleep(4)
links = driver.find_elements(By.TAG_NAME,('a'))   # to find the links available in current page
print(len(links)) #to print how many links available in page
for link in links: #run loop to print all link keyword in result section
    print(link.text)