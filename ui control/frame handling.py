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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear() #unable to locate the element error meanmight be htere FRAME
driver.find_element(By.ID,"tinymce").send_keys("first frame test")
