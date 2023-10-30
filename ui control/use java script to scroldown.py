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
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #executive_script method use to excute java script
#driver.get_screenshot_as_file("screenimage.png")

