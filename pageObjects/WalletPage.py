from selenium.webdriver.common.by import By



class GetWalletPage:
    def __init__(self,driver):
        self.driver = driver
    currentBalance = (By.XPATH, "(//p[@id='wallet-price'])[1]")
    contactMenu = (By.XPATH, "(//span[@class='menu-name'])[1]")
    addContact = (By.XPATH, "(//button[@class='add-contact'])[2]")
    addPaymentManual = (By.CSS_SELECTOR, "label[for='payment_manually']")
    sendNow = (By.CSS_SELECTOR,"div[class='stepper-body send-mony-stepper-slide-onee'] span[class='mdc-button__label']")
    continueButton = (By.XPATH, "(//span[@class='mdc-button__label'])[1]")
    selectBeneficiary = (By.XPATH, "//mat-select[@placeholder='Select beneficiary']")
    searchBeneficiary = (By.CSS_SELECTOR, "input[placeholder='Search']")
    clickSelected = (By.XPATH, "(//mat-option[@role='option'])[1]")
    letsContinue = (By.CSS_SELECTOR,"div[class='stepper-body send-mony-stepper-slide-two'] span[class='mdc-button__label']")
    beneficiaryAmount = (By.ID, "beneficiaryAmount-field")
    feeText = (By.CSS_SELECTOR, "span[class='regular-text ng-star-inserted'] span")
    checkBox = (By.XPATH, "(//div[@class='mdc-checkbox'])[1]")
    confirmButton = (By.XPATH, "(//span[@class='mdc-button__label'])[2]")
    confirmSelectCheckBox = (By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
    sendPaymentButton = (By.XPATH, "(//span[@class='mdc-button__label'])[3]")
    confirmPaymentText = (By.XPATH, "//h6[normalize-space()='You have sent a payment of']")
    backToMainPage = (By.CLASS_NAME, "form-link")
    tempBalance = (By.XPATH, "(//p[@id='wallet-price'])[1]")

    def CurrentBalance(self):
        return self.driver.find_element(*GetWalletPage.currentBalance)
    def GetWalletPage(self):
        return self.driver.find_element(*GetWalletPage.contactMenu)

    def MenueContact(self):
        return self.driver.find_element(*GetWalletPage.addContact)
    def ManualPayment(self):
        return self.driver.find_element(*GetWalletPage.addPaymentManual)

    def SendNowArea(self):
        return self.driver.find_element(*GetWalletPage.sendNow)

    def ContinueButton(self):
        return self.driver.find_element(*GetWalletPage.continueButton)

    def SelectBeneficiary(self):
        return self.driver.find_element(*GetWalletPage.selectBeneficiary)

    def SearchBeneficiary(self):
        return self.driver.find_element(*GetWalletPage.searchBeneficiary)

    def ClickSelected(self):
        return self.driver.find_element(*GetWalletPage.clickSelected)

    def LetsContinue(self):
        return self.driver.find_element(*GetWalletPage.letsContinue)

    def BeneficiaryAmount(self):
        return self.driver.find_element(*GetWalletPage.beneficiaryAmount)

    def FeeText(self):
        return self.driver.find_element(*GetWalletPage.feeText)

    def CheckBox(self):
        return self.driver.find_element(*GetWalletPage.checkBox)

    def ConfirmButton(self):
        return self.driver.find_element(*GetWalletPage.confirmButton)

    def ConfirmSelectCheckBox(self):
        return self.driver.find_element(*GetWalletPage.confirmSelectCheckBox)

    def SendPaymentButton(self):
        return self.driver.find_element(*GetWalletPage.sendPaymentButton)

    def ConfirmPaymentText(self):
        return self.driver.find_element(*GetWalletPage.confirmPaymentText)

    def BackToMainPage(self):
        return self.driver.find_element(*GetWalletPage.backToMainPage)

    def TempBalance(self):
        return self.driver.find_element(*GetWalletPage.tempBalance)