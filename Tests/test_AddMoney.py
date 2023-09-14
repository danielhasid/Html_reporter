import time
from pytest_html_reporter import attach
import pytest
from selenium.webdriver.common.by import By
from TestData.LoginData import LoginDataTest
from pageObjects.Login import LogingDetails
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestAddMoney(BaseClass):

    def test_AddMoneyToWallet(self,GetData):
        login_page = LogingDetails(self.driver)
        login_page.UserName().send_keys(GetData["mail"])
        login_page.Password().send_keys(GetData["password"])
        login_page.SubmitButton().click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,"(//span[normalize-space()='Accounts'])[1]").click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]").click()
        self.driver.find_element(By.XPATH, "(//p[normalize-space()='From myself'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//label[@for='beneficiarAcc-0'])[1]").click()
        self.WaitUntilClickable(self.driver.find_element(By.XPATH, "(//label[@for='beneficiarAcc-0'])[1]"))
        self.driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Next'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "transferAmount-field").click()
        self.driver.find_element(By.ID, "transferAmount-field").send_keys("200")
        self.driver.find_element(By.XPATH, "(//label[@for='regularTransfer'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[19]").click()
        time.sleep(1)
        self.WaitUntilClickable((By.XPATH, "(//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'])[1]"))
        self.driver.find_element(By.XPATH, "(//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'])[1]").click()
        self.driver.find_element(By.ID, "button-continue").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "mdc-checkbox__native-control").click()
        self.driver.find_element(By.XPATH, "(//button[@id='button-next'])[2]").click()
        time.sleep(1)

        well_done = self.driver.find_element(By.XPATH, "(//h5[normalize-space()='Well done!'])[1]").text

        assert "done!" in well_done

        self.driver.find_element(By.CLASS_NAME, "form-link").click()


    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self, request):
        return request.param
    #
    #
    # def screenshot_on_failure(self):
    #     for self._testMethodName, error in self._outcome.errors:
    #         if error:
    #             attach(data=self.driver.get_screenshot_as_png())