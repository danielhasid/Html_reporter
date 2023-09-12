import time
from pytest_html_reporter import attach

import pytest

from TestData.LoginData import LoginDataTest

from pageObjects.ConverFlow import GetConvertFlow
from pageObjects.Login import LogingDetails
from utilities.BaseClass import BaseClass

summery_list = []


@pytest.mark.usefixtures("setup")
class TestConvert(BaseClass):
    def test_Convert(self,GetData):
        convert_flow = GetConvertFlow(self.driver)
        login_page = LogingDetails(self.driver)
        login_page.UserName().send_keys(GetData["mail"])
        login_page.Password().send_keys(GetData["password"])
        login_page.SubmitButton().click()
        time.sleep(5)

        convert_flow.GetWalletPage().click()

        time.sleep(1)
        convert_flow.ChargedWallet().click()
        Charged_wallet = convert_flow.ChargedWallet().text
        wallet_before = self.ReformatCurrency(Charged_wallet)
        balance = round(float(wallet_before),2)
        print(balance)
        convert_flow.ConvertButtonName().click()
        convert_win = convert_flow.ConvertMoney().text
        time.sleep(1)
        if "Convert" not in convert_win:
            print(f"You are not in {convert_win} page")

        convert_flow.ConvertNowArea().click()

        convert_flow.MakeItNowButton().click()
        time.sleep(2)

        convert_flow.RequestConvertAmountField().click()
        time.sleep(2)
        convert_flow.RequestConvertAmountField().send_keys('100')
        time.sleep(1)
        self.MoveByOffst()
        convert_flow.CountryDropDown().click()
        countries = convert_flow.Countries()

        for country in countries:
            if country.text == "EUR":
                country.click()
                break

        self.MoveByOffst()

        convert_flow.ConvertButton().click()

        time.sleep(2)


        check_box = convert_flow.CheckBox()
        check_box.click()
        time.sleep(2)
        convert_flow.SummaryButton().click()
        time.sleep(2)

        message = convert_flow.SummaryMessage()
        print(message.text)
        convert_flow.BackToWallet().click()

        print("Convert Scenario passed")


    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self, request):
        return request.param



