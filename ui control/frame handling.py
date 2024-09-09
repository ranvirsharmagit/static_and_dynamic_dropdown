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
driver.find_element(By.LINK_TEXT,"Click Here").click() #open new window
windowopen = driver.window_handles
time.sleep(2)
driver.switch_to.window(windowopen[1]) #switch to new window
driver.close() #close new open window
driver.switch_to.window(windowopen[0]) #back to first window
time.sleep(2)

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(5)
driver.switch_to.frame("mce_0_ifr") #for the iframe we have to switch to frame to test
driver.find_element(By.ID,"tinymce").clear() #unable to locate the element error meanmight be htere FRAME
driver.find_element(By.ID,"tinymce").send_keys("first frame test")
