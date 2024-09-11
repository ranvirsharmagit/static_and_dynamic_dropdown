import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
name="ranvir"
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert   #chapter -handling java script  alert box
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()  #to click ok on alertbox
time.sleep(3)