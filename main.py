import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#staticdropdown
#driver.find_element(By.LINK_TEXT,"Forgot Password?")
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)
#dropdown.select_by_value()

#dynamicdropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") #list of countries check here
print(len(countries)) #to count countries available in list

for country in countries: #by this we select a country for field
    if country.text == "India":
        country.click()
time.sleep(2)

#print(driver.find_element(By.ID,"autosuggest").text)
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"







