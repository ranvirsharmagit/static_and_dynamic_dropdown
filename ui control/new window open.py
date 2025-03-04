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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
window_open = driver.window_handles

driver.switch_to.window(window_open[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

