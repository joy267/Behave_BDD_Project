from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I get navigated to Home page')
def homepage(context):

    expected_title = "Your Store"
    assert context.driver.title.__eq__(expected_title)


@when(u'I enter a valid product in the search box field')
def valid_products(context):
    context.driver.find_element(By.NAME, "search").send_keys("hp")


@when(u'I click the search button')
def search_button(context):
    context.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()


@then(u'Validate the product should displayed in search result')
def final_result(context):
    assert context.driver.find_element(By.PARTIAL_LINK_TEXT, "HP").is_displayed()


@when(u'I enter a invalid product in the search box field')
def invalid_products(context):
    context.driver.find_element(By.NAME, "search").send_keys("honda")


@then(u'Validate the proper message should displayed in search result')
def final_message(context):
    expected_message = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")\
        .text.__eq__(expected_message)
    context.driver.quit()


@when(u'I do not enter any value in the search box')
def blank_value(context):
    context.driver.find_element(By.NAME, "search").send_keys("")