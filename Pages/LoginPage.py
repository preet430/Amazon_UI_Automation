import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass

class LoginPage(BaseClass) :

    def __init__(self, driver):
        self.driver = driver

    signin_screen_btn = (By.XPATH, "//div[@id='nav-link-accountList']")
    mobile_box = (By.ID, "ap_email_login")
    continue_btn = (By.CLASS_NAME, "a-button-input")
    password_box = (By.ID, "ap_password")
    mobile_validation_alert = (By.XPATH, "//div[contains(text(),'Invalid mobile number')]")
    password_validation_alert = (By.XPATH, "//div[@class='a-section a-spacing-base auth-pagelet-container']//div[@class='a-box-inner a-alert-container']//div[1]")
    signin_btn = (By.CSS_SELECTOR, "#signInSubmit")

    #Signin screen open
    def open_signin(self):
        self.driver.find_element(*LoginPage.signin_screen_btn).click()

    #Signin with invalid mobile number
    def invalid_mobile(self, invalid_mobile):
        self.driver.find_element(*LoginPage.mobile_box).send_keys(invalid_mobile)
        self.driver.find_element(*LoginPage.continue_btn).click()
        time.sleep(5)
        mobile_validation_message = self.driver.find_element(*LoginPage.mobile_validation_alert).text
        print("Validation Message:", mobile_validation_message)
        assert "Invalid mobile number" in mobile_validation_message
        self.driver.find_element(*LoginPage.mobile_box).clear()

    #Signin with invalid password
    def invalid_password(self, valid_mobile, invalid_psw):
        self.driver.find_element(*LoginPage.mobile_box).send_keys(valid_mobile)
        self.driver.find_element(*LoginPage.continue_btn).click()
        self.driver.find_element(*LoginPage.password_box).send_keys(invalid_psw)
        self.driver.find_element(*LoginPage.signin_btn).click()
        time.sleep(5)
        password_validation_message = self.driver.find_element(*LoginPage.password_validation_alert).text
        assert "Your password is incorrect" in password_validation_message

    #Signin with valid password
    def valid_password(self, valid_psw):
        self.driver.find_element(*LoginPage.password_box).send_keys(valid_psw)
        self.driver.find_element(*LoginPage.continue_btn).click()

    #In first attempt sign in with valid credentials
    def valid_login(self, valid_mobile, valid_psw):
        self.driver.find_element(*LoginPage.mobile_box).send_keys(valid_mobile)
        self.driver.find_element(*LoginPage.continue_btn).click()
        self.driver.find_element(*LoginPage.password_box).send_keys(valid_psw)
        self.driver.find_element(*LoginPage.signin_btn).click()