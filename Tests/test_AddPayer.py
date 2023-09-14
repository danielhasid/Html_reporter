import time
from pytest_html_reporter import attach
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver import ActionChains


from selenium.webdriver.support.wait import WebDriverWait

from TestData.LoginData import LoginDataTest
from pageObjects.Login import LogingDetails

from utilities.BaseClass import BaseClass
from utilities.DB import TestDeleteUser

country_list = []
IbanNumber = 'IL220311810000000169803'
element = ''
@pytest.mark.usefixtures("setup")

class TestAddBeneficiary(BaseClass):
    def exist_element(self):
        try:
            self.driver.find_element(By.XPATH, "(//img[@class='currenyImage'])[1]")
        except NoSuchElementException:
            return False

    def test_TestAddPayer(self ,GetData):
        # payer = "Daniel Automation Payer Test"
        # sql = TestDeleteUser()
        # log = self.get_Logger()
        login_page = LogingDetails(self.driver)
        login_page.UserName().send_keys(GetData["mail"])
        login_page.Password().send_keys(GetData["password"])
        login_page.SubmitButton().click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Contacts'])[1]").click()
        self.driver.find_element(By.CLASS_NAME, "add-contact").click()
        self.driver.find_element(By.XPATH, "(// p[normalize-space() = 'Payer'])[1]").click()
        self.MoveByOffst()
        self.driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Next'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//label[@for='myAccounts'])[1]").click()
        # self.WaitUntilClickable(By.XPATH, "(//button[@type='submit'])[2]")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        self.driver.find_element(By.XPATH, "(//label[@for='myAccountsIsrael'])[1]").click()
        self.driver.find_element(By.ID, "bankCode").send_keys("31")
        self.driver.find_element(By.ID, "bankBranch").send_keys("181")
        time.sleep(1)
        self.driver.find_element(By.NAME,"bankAccountNumber").send_keys("169803")
        time.sleep(2)
        #
        # try:
        #     element = self.driver.find_element(By.XPATH, "(//input[@name='ibanNumber'])[1]").text
        #     print("The element exists.")
        #     assert IbanNumber == element
        # else:
        # except NoSuchElementException:
        #     print("The element does not exist.")

        is_element_exists = self.exist_element()
        while is_element_exists:
            time.sleep(1)
            self.driver.find_element(By.NAME,"bankAccountNumber").clear()
            self.driver.find_element(By.NAME,"bankAccountNumber").send_keys("169803")
            is_element_exists = self.exist_element()

        self.driver.find_element(By.XPATH,"(//button[@class='next-button mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base ng-star-inserted'])[1]").click()

        # time.sleep(2)
        # assert "done!" == self.driver.find_element(By.XPATH,"(//h5[normalize-space()='Well done!'])[1]").text

        # count = sql.existPayer(payer)
        # try:
        #     if count == 1:
        #         log.info("New Payer added")
        # except Exception as err:
        #     log.info(err)



    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self, request):
        return request.param

