from selenium.webdriver.common.by import By

class Login:
    my_account_xpath = "//span[text() = 'My Account']"
    login_xpath = "//a[text() = 'Login']"
    email_id = "input-email"
    password_id = "input-password"
    login_btn_xpath = "//input[@value = 'Login']"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def enter_email(self, username):
        self.driver.find_element(By.ID, self.email_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        