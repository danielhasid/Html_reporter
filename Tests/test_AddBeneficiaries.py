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


@pytest.mark.usefixtures("setup")

class TestAddBeneficiary(BaseClass):

    def exist_element(self):
        try:
            self.driver.find_element(By.XPATH,"//*[@id='cdk-step-content-0-3']/app-add-edit-benificiary-step3/form/div[3]/div[2]/span")
        except NoSuchElementException:
            return False

    def test_TestAddBeneficiary(self,GetData):
        user = 'aotu@aotu.com'
        sql = TestDeleteUser()
        log = self.get_Logger()
        log.info("Going to delete user")
        log.info(sql.delete(user))
        login_page = LogingDetails(self.driver)
        login_page.UserName().send_keys(GetData["mail"])
        login_page.Password().send_keys(GetData["password"])
        login_page.SubmitButton().click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Contacts'])[1]").click()
        # Beneficiaries = self.driver.find_elements(By.CLASS_NAME, "mdc-tab__text-label")
        #
        # sum = 0
        # for i in Beneficiaries:
        #     sum = sum + 1
        #
        # assert sum == 2

        self.driver.find_element(By.XPATH, "(//span[contains(text(),'Beneficiaries')])[1]").click()
        self.driver.find_element(By.CLASS_NAME, "add-contact").click()

        # Boxes = self.driver.find_elements(By.CLASS_NAME, "box-radio")
        # sum = 0
        # for box in Boxes:
        #     sum = sum + 1
        #
        # assert sum == 2

        self.driver.find_element(By.XPATH, "(//p[normalize-space()='Beneficiaries'])[1]").click()
        self.MoveByOffst()
        self.driver.find_element(By.XPATH,"(//span[@class='mdc-button__label'][normalize-space()='Next'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//button[@class='mat-stepper-next skip-btn mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base ng-star-inserted'])[1]").click()

        self.driver.find_element(By.ID, "bankAccountHolderName").send_keys("Automation holder")
        self.driver.find_element(By.ID, "bankAccountHolderEmail").send_keys("aotu@aotu.com")

        account_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-select-value-5")))
        account_btn.click()

        # driver.find_element(By.CLASS_NAME,"mat-mdc-select-arrow ng-tns-c83-11").click()

        countries = self.driver.find_elements(By.CLASS_NAME, "mdc-list-item__primary-text")

        for country in countries:
            if country.text == "Israel":
                country.click()
                break
        try:
            assert "Bank account holder name (Hebrew only)" == self.driver.find_element(By.XPATH,
                                                                                   "(//label[normalize-space()='Bank account holder name (Hebrew only)'])[1]").text
        except:
            print("No hebrew in the text")

        self.driver.find_element(By.ID, "bankAccountHolderHebrewName").send_keys("אוטומציה")
        self.driver.find_element(By.XPATH, "(//div[@id='mat-select-value-3'])[1]").click()
        time.sleep(1)
        classification = self.driver.find_elements(By.TAG_NAME, "mat-option")
        time.sleep(1)
        for i in classification:
            if i.text == "Company":
                i.click()
                break

        # self.MoveToElement((By.XPATH,"//*[@id='mat-select-value-7']/span"))
        # self.driver.find_element(By.XPATH,"//*[@id='mat-select-value-7']/span").click()
        self.WaitUntilClickable((By.XPATH, "(//div[@id='mat-select-value-7'])[1]"))
        self.driver.find_element(By.XPATH, "(//div[@id='mat-select-value-7'])[1]").click()
        # self.driver(By.XPATH,"(//span[normalize-space()='Central District'])[1]").click()
        states = self.driver.find_elements(By.TAG_NAME, "mat-option")
        for state in states:
            if "Central" in state.text:
                state.click()
                break

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//mat-select[@name='beneficiaryCity']//div[2]").click()

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/mat-option[2]").click()

        self.driver.find_element(By.ID, "beneficiaryStreet").send_keys("this my street")

        self.driver.find_element(By.ID, "beneficiaryHouseNumber").send_keys("1")

        self.driver.find_element(By.ID, "beneficiaryZipCode").send_keys("12345")

        self.driver.find_element(By.ID, "beneficiaryIdNumber").send_keys("133345346")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[4]").click()

        self.driver.find_element(By.XPATH,"(//label[@for='swift'])[1]").click()


        time.sleep(1)
        input_swift = self.driver.find_element(By.XPATH, "//input[@id='swiftCode']")
        time.sleep(1)
        input_swift.send_keys("POALILIT")

        is_element_exists = self.exist_element()
        while is_element_exists:
            time.sleep(1)
            input_swift.clear()
            input_swift.send_keys("POALILIT")
            is_element_exists = self.exist_element()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "bankCountry")))
        time.sleep(1)
        bank_number = self.driver.find_element(By.XPATH, "//input[@id='bankNumber']")
        bank_number.send_keys("122344")
        account_number = self.driver.find_element(By.XPATH, "//input[@id='accountNumber']")
        account_number.send_keys("45454545")
        # driver.find_element(By.CLASS_NAME,"mat-mdc-select-value ng-tns-c83-14").click()
        # ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        self.driver.find_element(By.XPATH,
                            "//body/div/div[@dir='ltr']/div/mat-dialog-container[@role='dialog']/div/div/app-add-contacts/mat-dialog-content/div/form/mat-stepper[@role='tablist']/div/div/div[@role='tabpanel']/app-add-edit-benificiary-step3/form/div/div/div/div/div/mat-select[@name='currency']/div/div[1]").click()

        all_currencies = self.driver.find_elements(By.TAG_NAME, "mat-option")
        for currency in all_currencies:
            time.sleep(1)
            if currency.text == "EUR":
                currency.click()
                break

        time.sleep(1)

        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[5]").click()

        # paymrnt to service
        self.driver.find_element(By.XPATH, "//label[@for='paymentOfService']").click()

        time.sleep(1)
        self.driver.find_element(By.XPATH,"//body/div/div[@dir='ltr']/div/mat-dialog-container[@role='dialog']/div/div/app-add-contacts/mat-dialog-content/div/form/mat-stepper[@role='tablist']/div/div/div[@role='tabpanel']/app-add-edit-benificiary-step4/form/div/div/div/div/mat-select[@placeholder='Select from list']/div[1]").click()

        # driver.find_element(By.XPATH,"(//mat-select[@placeholder='Select from list'])[1]").click()

        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Third Party Transfer'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Make it now'])[1]").click()
        self.WaitUntilClickable((By.XPATH, "(//button[@type='submit'])[6]"))
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[6]").click()

        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Back to my contacts'])[1]").click()
        count = sql.existUser(user)
        try:
            if count == 1:
                log.info("New Beneficiary added")
        except Exception as err:
            log.info(err)





    @pytest.fixture(params=LoginDataTest.LoginData)
    def GetData(self, request):
        return request.param





