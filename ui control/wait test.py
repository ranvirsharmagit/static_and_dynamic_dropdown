import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(9)
 #apply time wait to all driver step
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

#time.sleep(4)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("ranvir")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
#time.sleep(6) time sleep we use when for specific step ew need some time
#explcitwaittime use for when on specific condition we need some extra time to wait after apply impecit wait on the page to perfrm or execute some step.
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoinfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoinfo").text);
