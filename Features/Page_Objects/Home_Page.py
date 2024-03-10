from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_option_class = "dropdown"
    login_option_click = "Login"
    register_option_click = "Register"


    def click_on_my_account(self):
        self.driver.find_element(By.CLASS_NAME, self.my_account_option_class).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_click).click()

    def select_registration_option(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.register_option_click).click()