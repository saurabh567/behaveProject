import time

import driver
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on the Gear link')
def step_impl(context):
    action = ActionChains(context.driver)
    m = context.driver.find_element(By.XPATH, "//span[contains(.,'Gear')]")
    action.move_to_element(m).perform()
    time.sleep(5)



@then(u'go to the jacket and click on it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then go to the jacket and click on it')


@then(u'category page related to jacket opens up')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then category page related to jacket opens up')


@then('navigate to the category URL')
def step_impl(context):
    context.driver.get("https://kumar-saurabh.pixelmechanics-dev.de/women/bottoms-women/pants-women.html")
    context.driver.maximize_window()
    time.sleep(3)


@then('select each option under the shopping options')
def step_impl(context):
    shopping_options = context.driver.find_elements(By.XPATH, "//div[contains(@class,'filter-options-title')]")
    for shopping_option in shopping_options:
        shopping_option.click()
        time.sleep(3)


@then('click on the capri under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'Capri')])[7]").click()
    time.sleep(3)


@then('click on the size  under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//div[@class='swatch-option text '])[2]").click()
    time.sleep(3)


@then('click on the climate under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(.,'Warm')]").click()
    time.sleep(3)


@then('click on the color under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//div[@class='swatch-option color '])[4]").click()
    time.sleep(3)


@then('click on the eco collection under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'No')])[1]").click()
    time.sleep(3)


@then('click on the erin recommends under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'No')])[2]").click()
    time.sleep(3)


@then('click on the material under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(.,'Microfiber')]").click()
    time.sleep(3)


@then('click on the new under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'No')])[3]").click()
    time.sleep(3)


@then('click on the pattern under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(.,'Color-Blocked')]").click()
    time.sleep(3)


@then('click on the performance fabric under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'No')])[4]").click()
    time.sleep(3)


@then(u'click on the price under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'-')])[4]").click()
    time.sleep(3)


@then('click on the sale under style shopping options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//div[contains(@class,'filter-options-title')])[1]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//a[contains(.,'No')])[5]").click()
    time.sleep(3)


@then('click on the sort by toggle down option Price')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//select[@id='sorter']//option[3]").click()
    time.sleep(3)


@then('click on the list mode of viewing')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//div[@class='modes']//strong[@title='List']").click()
    time.sleep(3)


@then('click on the Grid mode of viewing')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='modes']//a[@title='Grid']").click()
    time.sleep(3)


@then('click on toggle down icon of number of products per page')
def step_impl(context):
    sel = Select(context.driver.find_element(By.XPATH, "//select[@id='limiter']"))
    sel.select_by_index(1)
    time.sleep(2)


@then('finding the total number of products on the category page')
def step_impl(context):
    total_products = (context.driver.find_elements(By.XPATH, "//span[@class='product-image-wrapper']"))
    print(len(total_products))
    print("saurabh")
    # for total_product in total_products1:
    #     print(total_product.text())
    #     time.sleep(7)

