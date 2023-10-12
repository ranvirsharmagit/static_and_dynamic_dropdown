#just copy and past code not working need some correction"Read data From Excel
import time

import username
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

FileInputStream file = new FileInputStream("C://TestData.xlsx");
Workbook workbook = new XSSFWorkbook (fle);
Sheet sheet = workbook. getSheetAt(0);
#Loop through rows in Excel sheet
for (int 1 = 1; 1 <= sheet-getLastRowNum); 1++) {
Row row = sheet-getRow(1);
String username • row-getCell(1) getStringCellvalue;
eString password = row-getCell(2) -getStringCellValue();
# Open the application
driver-get (https://secure04ea.chase.com/
veb/auth/#/logon/logon/chaseOnline?treatment=chase&lang=en");
# Perform login with data from Excel
driver. findElement (By.id ("username")). sendkeys (username);
driver. findElement (By.id ("password")) . sendKeys (password);
driver. findElement (By.id("loginButton")). click();