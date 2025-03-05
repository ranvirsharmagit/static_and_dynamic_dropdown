import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
titile = driver.title
driver.maximize_window() #for maximize the window
driver.implicitly_wait(5)
driver.get("https://training.pfms.gov.in/SitePages/Users/LoginDetails/Login.aspx")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #executive_script method use to excute java script
time.sleep(5)
driver.get_screenshot_as_file("screenimage.png")
print (titile)
