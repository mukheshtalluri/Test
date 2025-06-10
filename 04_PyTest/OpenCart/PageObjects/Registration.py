from selenium.webdriver.common.by import By


class Register:
    my_account_xpath = "//span[text() = 'My Account']"
    register_xpath = "//a[text()='Register']"
    firstname_id = "input-firstname"
    lastname_id = "input-lastname"
    email_id = "input-email"
    phone_id = "input-telephone"
    password_id = "input-password"
    conform_password_id = "input-confirm"
    privacy_checkbox_xpath = "//input[@name = 'agree']"
    continue_register_xpath = "//input[@value = 'Continue']"
    account_created_xpath = "//h1[text() = 'Your Account Has Been Created!']"
    continue_xpath = "//a[text() = 'Continue']"
    logout_xpath = "//a[text() = 'Logout']"
    continue_logout_xpath = "//a[text() = 'Continue']"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_register(self):
        self.driver.find_element(By.XPATH, self.register_xpath).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def enter_emil(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, self.phone_id).send_keys(phone_number)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_conform_password(self, password):
        self.driver.find_element(By.ID, self.conform_password_id).send_keys(password)

    def click_privacy_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_checkbox_xpath).click()

    def click_register_button(self):
        self.driver.find_element(By.XPATH, self.continue_register_xpath).click()

    def registration_conform(self):
        reg_conform = self.driver.find_element(By.XPATH, self.account_created_xpath)
        return reg_conform

    def continue_registration(self):
        self.driver.find_element(By.XPATH, self.continue_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        self.driver.find_element(By.XPATH, self.continue_logout_xpath).click()