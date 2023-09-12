import time
from pytest_html_reporter import attach
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from TestData.LoginData import LoginDataTest
from pageObjects.Login import LogingDetails
from pageObjects.WalletPage import GetWalletPage
from utilities.BaseClass import BaseClass


class TestPayment(BaseClass):

    def test_payment_scenario(self,GetData):
        log = self.get_Logger()
        login_page = LogingDetails(self.driver)
        wallet_page = GetWalletPage(self.driver)
        log.info("Entering user name")
        login_page.UserName().send_keys(GetData["mail"])
        log.info("Entering password")
        login_page.Password().send_keys(GetData["password"])
        log.info("Submit User Data")
        login_page.SubmitButton().click()
        time.sleep(5)
        log.info("Receive the current balance")
        balance_temp = wallet_page.CurrentBalance().text
        balance_before = re.sub('[$,]', "", balance_temp)
        balance = float(balance_before)

        wallet_page.GetWalletPage().click()
        wallet_page.MenueContact().click()
        time.sleep(1)

        wallet_page.ManualPayment().click()
        log.info("Now payment request")
        wallet_page.SendNowArea().click()
        wallet_page.ContinueButton().click()
        time.sleep(1)
        wallet_page.SelectBeneficiary().click()

        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").send_keys("Test USD")
        time.sleep(2)
        wallet_page.ClickSelected().click()
        wallet_page.LetsContinue().click()

        wallet_page.BeneficiaryAmount().send_keys("100")

        wallet_page.BeneficiaryAmount().send_keys(Keys.TAB)
        time.sleep(5)
        temp_fee = wallet_page.FeeText().text
        fee = float(re.sub('[$]', "", temp_fee))
        if wallet_page.CheckBox().is_selected():
            print("Test failed checkBox was selected by default")
        wallet_page.CheckBox().click()
        time.sleep(2)

        wallet_page.ConfirmButton().click()

        time.sleep(2)

        if wallet_page.ConfirmSelectCheckBox().is_selected():
            print("Test failed checkBox was selected by default")
        wallet_page.ConfirmSelectCheckBox().click()
        time.sleep(2)
        wallet_page.SendPaymentButton().click()

        time.sleep(3)
        result = wallet_page.ConfirmPaymentText().text
        print(result)

        wallet_page.BackToMainPage().click()
        time.sleep(2)
        balance_temp = wallet_page.TempBalance().text
        balance_after = float(re.sub('[$,]', "", balance_temp))

        wallet_charged = int(balance - balance_after)
        print(wallet_charged)
        if wallet_charged == int(100 + fee):
            print("Payment scenario passed")
            log.info("Payment test scenario passed")

    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self,request):
        return request.param



