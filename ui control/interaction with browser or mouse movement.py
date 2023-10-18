import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window() #for maximize the window
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver) #use for many purpose like hover and many more
#action.double_click(driver.find_element(By.XPATH,"sdfsjkdjslkd")) use for double click on anything
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform() use for right click on element
time.sleep(4)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click()
