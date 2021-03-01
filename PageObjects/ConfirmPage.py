from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    findCountry = (By.ID, "country")
    confirmCountry = (By.LINK_TEXT, "United States of America")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CSS_SELECTOR, "[class*='alert-succes']")

    def getFindCountry(self):
        return self.driver.find_element(*ConfirmPage.findCountry)

    def getConfirmCountry(self):
        return self.driver.find_element(*ConfirmPage.confirmCountry)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText).text
