from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self,driver):
        self.driver = driver


    account_page_id = "content"


    def account_page_verfication(self):
        return self.driver.find_element(By.ID, self.account_page_id).is_displayed()