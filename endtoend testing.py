import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
productslist = driver.find_elements(By.XPATH,"//div[@class='card h-100']") #create xpath for all product list so we can find blackberry from this class name for ach product is same so we create by card class name

for product in productslist :
    ProductName = product.find_element(By.XPATH,"div/h4/a").text     #we use product.find_element because we use chaining method
    if ProductName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()  #if we use *after class then we use partial value of class name
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ind")
wait = WebDriverWait(driver,10)    #to give time to load country name list
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))   #wait till meet this condition or India appear in list
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class*=checkbox]").click()     #use of * in CSS when you want to choose partial class name
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Sucsses = driver.find_element(By.CSS_SELECTOR,"div[class*=alert]").text

assert "Success! Thank you!" in Sucsses   # use "in" instead of == in assertion because given keyword must appear in list if we select == then exact keyword should appear

print(Sucsses)
