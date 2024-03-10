from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_address_field = "input-email"
    password_field = "input-password"
    login_button = "//input[@value='Login']"
    warning_message= "//div[@id= 'account-login'] /div[1]"

    def enter_email_address(self,email_text_value):
        self.driver.find_element(By.ID,self.email_address_field).send_keys(email_text_value)

    def enter_password(self,password_text):
        self.driver.find_element(By.ID, self.password_field).send_keys(password_text)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def warning_message_status(self,warning_text):
        return self.driver.find_element(By.XPATH, self.warning_message).text.__contains__(warning_text)