from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://parabank.parasoft.com/parabank/index.htm')

driver.get('https://automationintesting.online/')

driver.back()

driver.refresh()

driver.forward()