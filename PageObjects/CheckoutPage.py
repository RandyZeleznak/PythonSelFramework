from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
    
    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    initialCheckOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getInitialCheckOut(self):
        return self.driver.find_element(*CheckoutPage.initialCheckOut)

    def getCheckOut(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage