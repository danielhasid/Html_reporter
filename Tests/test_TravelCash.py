import datetime
import re
from pytest_html_reporter import attach

import time

import pytest
from selenium.webdriver.common.by import By

from TestData.LoginData import LoginDataTest
from pageObjects.ConverFlow import GetConvertFlow
from pageObjects.Login import LogingDetails
from pageObjects.WalletPage import GetWalletPage
from utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("setup")
class TestTravelCash(BaseClass):
    def test_TravelCash(self,GetData):
        amount = 100
        log = self.get_Logger()
        timeNow = datetime.datetime.now()
        if timeNow < self.todayAt(16):
            log.info("Running the test")
        else:
            log.info("Skipping Cash Travel test the time is after 16:00")
            pytest.skip("Skipping Cash Travel test the time is after 16:00")
        login_page = LogingDetails(self.driver)
        login_page.UserName().send_keys(GetData["mail"])
        login_page.Password().send_keys(GetData["password"])
        login_page.SubmitButton().click()
        time.sleep(5)

        # self.MoveToElement(self.driver.findelement(By.ID,"/html/body/app-root/div/div/app-home/div/div[2]/div[2]/div[1]/a"))
        self.driver.find_element(By.XPATH,"(//a[@id='cashToFlight-link'])[1]").click()
        # self.WaitUntilClickable(self.driver.find_element(By.ID, "datepicker-toggle-id"))
        self.driver.find_element(By.ID, "datepicker-toggle-id").click()
        self.MoveToElement(self.driver.find_element(By.XPATH,"(//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'])[1]"))
        self.driver.find_element(By.XPATH,"(//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'])[1]").click()
        self.MoveToElement(self.driver.find_element(By.ID,"amount-id"))
        self.driver.find_element(By.ID,"amount-id").send_keys(amount)
        self.WaitUntilClickable(self.driver.find_element(By.ID,"next-btn"))
        self.driver.find_element(By.ID, "next-btn").click()
        self.WaitUntilClickable(self.driver.find_element(By.ID, "hebrewName"))
        self.driver.find_element(By.ID, "hebrewName").send_keys("אטוטמציה")
        self.driver.find_element(By.ID, "idNumber").send_keys("999999998")
        self.driver.find_element(By.ID, "englishFirstName").send_keys("Automation Test")
        self.driver.find_element(By.ID, "englishLastName").send_keys("Python")
        self.driver.find_element(By.ID, "mobile").send_keys("0531231234")
        self.driver.find_element(By.ID, "email").send_keys("auto@gmai.com")
        self.WaitUntilClickable(self.driver.find_element(By.XPATH, "(//button[@id='next-button'])[1]"))
        self.driver.find_element(By.XPATH, "(//button[@id='next-button'])[1]").click()
        time.sleep(2)
        summary_amount = self.driver.find_element(By.XPATH,"(//span[@id='amount-id'])[1]").text
        print(summary_amount)
        travel_amount = re.sub('[$₪,]', "", summary_amount)
        log.info("The Summary amount is %s" ,travel_amount)

        assert int(amount) == int(travel_amount)

        self.driver.find_element(By.XPATH,"(//button[@id='next-button'])[2]").click()









    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self,request):
        return request.param
