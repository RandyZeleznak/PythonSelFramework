from telnetlib import EC

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.HomePage import HomePage
from PageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_endToEnd(self, setup):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutPage = homepage.shopItems()
        log.info("Getting all the card Titles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.getInitialCheckOut().click()

        confirmPage = checkoutPage.getCheckOut()
        log.info("Entering to search for country name")
        confirmPage.getFindCountry().send_keys("united")
        self.verifyLinkPresence("United States of America")
        confirmPage.getConfirmCountry().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSubmit().click()
        textMatch = confirmPage.getSuccessText()
        log.info("Screen Text received is " +textMatch)

        assert ("Success! Thank you!" in textMatch)
