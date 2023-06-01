from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver  = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_win32")

    @when('open the flipkart page')
    def openFlipkartPage(context):
        context.driver.get("https://www.flipkart.com/")

        @then('verify the flipkart logo present on the page')
        def verifyFlipkartLogo(context):
            status=context.driver.find_element(By.XPATH, "//img[@title='Flipkart']").is_displayed()
            assert status is True

            @then('close the browser')
            def closeBrowser(context):
                context.driver.close()


#Author kumar Saurabh