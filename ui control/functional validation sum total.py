import time

import total
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#list itemcheck
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver = webdriver.Chrome()
driver.implicitly_wait(9)
 #apply time wait to all driver step
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2) #use time lapse here because there "find.elements we use insted find.element"
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedList == actualList
#time.sleep(4)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()

#sum validation incart
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p") #somemore option css- td:nth-child(5) p xpath //tr/td[5]/p also //td[5]/p
sum = 0
for price in prices:
    sum = sum + int(price.text)
#print(sum)
#totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
#assert totalamount == sum
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
time.sleep(5)
afterdiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(afterdiscount)
assert totalamount > afterdiscount

#time.sleep(6) time sleep we use when for specific step ew need some time
#explcitwaittime use for when on specific condition we need some extra time to wait after apply impecit wait on the page to perfrm or execute some step.
#wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoinfo")))
#print(driver.find_element(By.CSS_SELECTOR,".promoinfo").text);



