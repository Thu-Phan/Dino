
from selenium import webdriver

driver = webdriver.Chrome("C:\D\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')


#driver.close()