import pytest
from py import log
from selenium.webdriver.support.select import Select
from selenium import webdriver

from PageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        log.info("Full Name : " + getData["fullname"])
        homePage.getName().send_keys(getData["fullname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getExampleCheck().click()
        self.selectOptionsByText(homePage.getGender(),getData["gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccess().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Home_Page_Data)
    def getData(self, request):
        return request.param
