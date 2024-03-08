from selenium import webdriver

from Utilites import ConfigReader


def before_scenario(context,driver):     # Before Hook method - For perform this steps before scenario

    browser_name  = ConfigReader.read_configuration("basic info" , "browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()


    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context,driver):         # After Hook method - For perform this steps after scenario

    context.driver.quit()