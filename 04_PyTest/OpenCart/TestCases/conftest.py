import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching chrome browser...')
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('Launching edge browser...')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Launching firefox browser...')
    else:
        print('Please select the appropriate browser.')
    return driver