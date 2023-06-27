import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_win32")


@when('open the prodinger page')
def step_impl(context):
    context.driver.get("https://kumar-saurabh.pixelmechanics-dev.de/")
    context.driver.maximize_window()


@then('enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "(//input[@type='email'])[1]").send_keys(user)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(pwd)


@then('click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")


# @then('user must successfully login  to the homepage')
# def step_impl(context):


@then('close the chrome browser')
def closeBrowser(context):
    context.driver.close()
