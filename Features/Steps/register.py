from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By

from Features.Page_Objects.Home_Page import HomePage


@given(u'I navigated to the register page')
def register_page(context):

    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    home_page.select_login_option()

    # context.driver.find_element(By.CLASS_NAME, "dropdown").click()
    # context.driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()


@when(u'I give the inputs into the mandatory fields')
def mandatory_inputs(context):

    first_name = context.driver.find_element(By.ID, "input-firstname").send_keys("test first name")
    last_name = context.driver.find_element(By.ID, "input-lastname").send_keys("test last name")
    email = context.driver.find_element(By.ID, "input-email").send_keys("dsfgfg@gmail.com")
    telephone = context.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
    password = context.driver.find_element(By.ID, "input-password").send_keys("1234")
    confirm_password = context.driver.find_element(By.ID, "input-confirm").send_keys("1234")
    privacy_policy = context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on continue button')
def continue_button(context):

    button = context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'Account should be created')
def account_create(context):

    expected_error = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@class='col-sm-9']/h1").text.__eq__(expected_error)


@when(u'I give the inputs into all the fields without email fields')
def step_impl(context):

    first_name = context.driver.find_element(By.ID, "input-firstname").send_keys("test first name")
    last_name = context.driver.find_element(By.ID, "input-lastname").send_keys("test last name")
    telephone = context.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
    password = context.driver.find_element(By.ID, "input-password").send_keys("1234")
    confirm_password = context.driver.find_element(By.ID, "input-confirm").send_keys("1234")
    privacy_policy = context.driver.find_element(By.NAME, "agree").click()



@when(u'I give existing email account in the email fields')
def step_impl(context):

    first_name = context.driver.find_element(By.ID, "input-firstname").send_keys("test first name")
    last_name = context.driver.find_element(By.ID, "input-lastname").send_keys("test last name")
    email = context.driver.find_element(By.ID, "input-email").send_keys("jnnkmmk@gmail.com")
    telephone = context.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
    password = context.driver.find_element(By.ID, "input-password").send_keys("1234")
    confirm_password = context.driver.find_element(By.ID, "input-confirm").send_keys("1234")
    privacy_policy = context.driver.find_element(By.NAME, "agree").click()



@then(u'Proper error message should be displayed for without email address')
def account_create(context):

    output = "E-Mail Address does not appear to be valid!"
    assert context.driver.find_element(By.CLASS_NAME, "text-danger").text.__eq__(output)


@then(u'Proper error message should be displayed for duplicate email address')
def duplicate_email(context):

    duplicate_email_error = "Warning: E-Mail Address is already registered!"

    assert context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(duplicate_email_error)




@when(u'I do not give any inputs into the fields')
def step_impl(context):

    privacy_policy = context.driver.find_element(By.NAME, "agree").click()


@then(u'Proper error message should be displayed')
def field_error_message(context):

    expected_first_name = "First Name must be between 1 and 32 characters!"
    expected_last_name = "Last Name must be between 1 and 32 characters!"
    expected_email = "E-Mail Address does not appear to be valid!"
    expected_telephone = "Telephone must be between 3 and 32 characters!"
    expected_password = "Password must be between 4 and 20 characters!"

    assert context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div")\
        .text.__eq__(expected_first_name)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div") \
        .text.__eq__(expected_last_name)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div") \
        .text.__eq__(expected_email)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div") \
        .text.__eq__(expected_telephone)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div") \
        .text.__eq__(expected_telephone)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div") \
        .text.__eq__(expected_password)

