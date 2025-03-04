#import Package
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wk = openpyxl.load_workbook("/Users/ranvirkumarsharma/PycharmProjects/extracting text from web page/ui control/excel/FINANCE PORTFOLIO .xlsx")
print(wk.sheetnames)
print(wk.active.title)