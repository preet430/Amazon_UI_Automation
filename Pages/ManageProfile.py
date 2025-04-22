import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

from Tests.conftest import driver
from Utilities.BaseClass import BaseClass

class ManageProfile(BaseClass) :

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1")

    #Validate login user name after login
    def validate_user_name_header(self, login_user_first_name):
        login_user = self.driver.find_element(*ManageProfile.user_name).text
        assert login_user_first_name in login_user

    account_popup = (By.CSS_SELECTOR, "#nav-link-accountList")
    manage_profile_btn = (By.XPATH, "//button[text()='Manage Profiles']")
    view_btn = (By.XPATH, "//a[text()='View']")

    #Open your profile screen
    def open_manage_profile(self):
        actions = ActionChains(self.driver)
        element_to_hover = self.driver.find_element(*ManageProfile.account_popup)
        actions.move_to_element(element_to_hover).perform()
        self.driver.find_element(*ManageProfile.manage_profile_btn).click()
        self.driver.find_element(*ManageProfile.view_btn).click()

    profile_name = (By.XPATH, "//div[@class='profile-name desktop']")
    edit_btn = (By.XPATH, "//button[@class='edit-pencil-icon-button']")
    cross_icon = (By.XPATH, "//i[@class='a-icon a-icon-close']")
    cancel_btn = (By.CSS_SELECTOR, "#editProfileCancelButton")
    image_upload = (By.ID, "profile-preferences-avatar-upload-id")
    edit_user_name = (By.ID, "editProfileNameInputId")
    continue_btn = (By.XPATH, "//span[contains(text(),'Continue')]")
    edit_error_msg = (By.XPATH, "//span[text()='You must enter at least one character.']")

    #Validate username, open-close popup & Upload the profile image
    def update_user_details(self, user_full_name, image_path):
        profile_text = self.driver.find_element(*ManageProfile.profile_name).text
        assert user_full_name in profile_text
        self.driver.find_element(*ManageProfile.edit_btn).click()
        wait = WebDriverWait(self.driver, 10)
        cross_icon_el = wait.until(expected_conditions.element_to_be_clickable(ManageProfile.cross_icon))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cross_icon_el)
        cross_icon_el.click()
        self.driver.refresh()
        self.driver.find_element(*ManageProfile.edit_btn).click()
        self.driver.find_element(*ManageProfile.cancel_btn).click()
        self.driver.refresh()
        self.driver.find_element(*ManageProfile.edit_btn).click()
        file_input = self.driver.find_element(*ManageProfile.image_upload)
        file_input.send_keys(image_path)
        self.driver.implicitly_wait(5)
        self.driver.refresh()




