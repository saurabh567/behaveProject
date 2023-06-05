import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver  = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_ver114")

    @when('open the flipkart page')
    def openFlipkartPage(context):
        context.driver.get("https://www.flipkart.com/")
        context.driver.maximize_window()

        @then('verify the flipkart logo present on the page')
        def verifyFlipkartLogo(context):
            status=context.driver.find_element(By.XPATH, "//img1[@title='Flipkart']").is_displayed()
            assert status is True

            @then('close the browser')
            def closeBrowser(context):
                context.driver.close()
        @then('click on the popupclose button')
        def popupClose(context):
               time.sleep(5)
               context.driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()


        @then('click on the seller button')
        def clickOnCartButton(context):
            time.sleep(10)
            context.driver.find_element(By.XPATH, "//div[@class='go_DOp']//span[text()='Become a Seller']").click()
