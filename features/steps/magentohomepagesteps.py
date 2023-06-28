import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_win32")


@when('open the magento luma page')
def step_impl(context):
    context.driver.get("https://kumar-saurabh.pixelmechanics-dev.de/")
    context.driver.maximize_window()


@then('enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(user)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@name='login[password]']").send_keys(pwd)
    time.sleep(5)


@then('click on signin button of customer account page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//span[contains(text(),'Sign In')])[1]").click()
    time.sleep(5)
@then('click on signin button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'Sign In')])[1]").click()


@then('close the chrome browser')
def closeBrowser(context):
    context.driver.close()
    time.sleep(5)


@then('click on the action showcart button')
def clickOnActionshowcartbutton(context):
    context.driver.find_element(By.XPATH, "//div[@class='minicart-wrapper']").click()
    time.sleep(5)

    @then('get the title of the page')
    def getTitle(context):
        time.sleep(5)
        my_url=context.driver.current_url
        print(my_url)
        print("myself saurabh")
        time.sleep(5)


    @then(u'click here link to continue shopping')
    def clickherebutton(context):
        context.driver.find_element(By.XPATH,"//a[contains(.,'here')]").click()
        time.sleep(3)
        url = context.driver.current_url
        print(url)
        time.sleep(3)

