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


@then('click and type "bags"inside the search bar')
def searchfunctionality(context):
    search = context.driver.find_element(By.XPATH,"//input[@id='search']")
    search.send_keys("bags")
    context.driver.find_element(By.XPATH,"//button[@title='Search']").click()
    time.sleep(5)


@then('click on each of the header links to open them in a new tab')
def step_impl(context):
    header_links = context.driver.find_elements(By.XPATH,"//li[contains(@class,'level0')]")
    time.sleep(5)
    for header_link in header_links:
        header_link.click()
        time.sleep(3)
        context.driver.back()
        time.sleep(10)


@then('click on the About us link')
def aboutUs(context):
    context.driver.find_element(By.XPATH,"//a[contains(.,'About us')]").click()
    time.sleep(5)
    print(context.driver.current_url)
    print(context.driver.title)
    time.sleep(5)
    context.driver.back()
    time.sleep(5)


@then('click on the Customer service link')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[.='Customer Service']").click()
    context.driver.back()
    time.sleep(5)

@then('click on the Privacy and cookie policy link')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[.='Privacy and Cookie Policy']").click()
    context.driver.back()
    time.sleep(5)

@then('click on the Search Terms link')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[.='Search Terms']").click()
    context.driver.back()
    time.sleep(5)

@then('click on the Advanced Search link')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[.='Advanced Search']").click()
    context.driver.back()
    time.sleep(5)
    @then('click on the orders and Returns link')
    def step_impl(context):
        context.driver.find_element(By.XPATH, "//a[.='Orders and Returns']").click()
        context.driver.back()
        time.sleep(5)
    @then('click on the Contact us link')
    def step_impl(context):
        context.driver.find_element(By.XPATH, "//a[.='Contact Us']").click()
        context.driver.back()
        time.sleep(5)

# @then(u'click on the first product image')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, "//li[contains(.,'Radiant Tee')]").click()


@then('click on each of the different sizes box individually')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "(//div[@role='listbox'])[1]//div[text()='XS']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//div[@aria-checked='false'])[2]").click()
    context.driver.find_element(By.XPATH, "(//div[@aria-checked='false'])[3]").click()
    context.driver.find_element(By.XPATH, "(//div[@aria-checked='false'])[4]").click()
    context.driver.find_element(By.XPATH, "(//div[@aria-checked='false'])[5]").click()
    time.sleep(2)

# @then(u'navigate to the previous page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then navigate to the previous page')


@then('click on each of the colour swatches')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@aria-label='Blue']").click()
    context.driver.find_element(By.XPATH, "//div[@aria-label='Orange']").click()
    context.driver.find_element(By.XPATH, "(//div[@aria-label='Purple'])[1]").click()
    time.sleep(3)


@then('click add to cart button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//span[contains(.,'Add to Cart')])[1]").click()
    time.sleep(3)

@then('navigate to the counter quantity button to check the product has been added')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[@class='counter-number']").click()
    time.sleep(3)


@then('click on proceed to checkout')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[.='Proceed to Checkout']").click()
    time.sleep(3)

@then('click on Create an account link')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@id='idUZ4jec1F']").click()
    time.sleep(3)


@then('filling the personal information')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("alok")
    context.driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("sinha")
    time.sleep(3)

@then('filling the signin information')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@title='Email']").send_keys("alok.kumar@pixelmechanics.de")
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("sinha@123")
    context.driver.find_element(By.XPATH, "//input[@id='password-confirmation']").send_keys("sinha@123")
    time.sleep(3)
@then('click on the create an account button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[.='Create an Account']").click()
    time.sleep(5)


