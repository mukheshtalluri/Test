from selenium import webdriver

# Driver instance
driver = webdriver.Chrome()

# Launch the application
driver.get('https://parabank.parasoft.com/parabank/index.htm')

# Get page title
print(driver.title)

# Get current url
print(driver.current_url)

# Get page source
print(driver.page_source)

