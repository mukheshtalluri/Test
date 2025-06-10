from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demo.applitools.com/')

print(driver.find_element(By.ID, 'log-in').is_displayed())

print(driver.find_element(By.ID, 'username').is_enabled())

print(driver.find_element(By.XPATH, '//input[@type = "checkbox"]').is_selected())




