import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text(male)
