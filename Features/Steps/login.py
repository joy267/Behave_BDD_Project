from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By

from Features.Page_Objects.Home_Page import HomePage


@given(u'I navigated to the login page')
def login_page(context):

    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    home_page.select_login_option()

    # context.driver.find_element(By.CLASS_NAME, "dropdown").click()
    # context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter the valid email and password into the fields')
def Valid_credentials(context):

    context.driver.find_element(By.ID, "input-email").send_keys("234testuser123@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("1234")


@when(u'I click the login button')
def login_button(context):

    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should get logged in')
def logged_in(context):

    context.driver.find_element(By.ID, "content").is_displayed()


@when(u'I enter the valid email and invalid password into the fields')
def valid_email(context):

    context.driver.find_element(By.ID, "input-email").send_keys("ghghu@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("12345678")


@then(u'I should get proper warning message')
def warning_message(context):

    error_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH, "//div[@id= 'account-login'] /div[1]").text.__contains__(error_message)



@when(u'I enter the invalid email and valid password into the fields')
def valid_password(context):

    context.driver.find_element(By.ID, "input-email").send_keys("234567testuser123@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("1234")


@when(u'I enter the invalid email and password into the fields')
def step_impl(context):

    context.driver.find_element(By.ID, "input-email").send_keys("testuser123@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("123456")
