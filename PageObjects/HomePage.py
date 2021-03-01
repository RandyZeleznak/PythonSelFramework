from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    home = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    exampleCheck = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.home)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getExampleCheck(self):
        return self.driver.find_element(*HomePage.exampleCheck)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)