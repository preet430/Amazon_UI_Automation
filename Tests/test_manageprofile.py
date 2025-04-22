import json

import pytest

from Pages.LoginPage import LoginPage
from Pages.ManageProfile import ManageProfile
from Utilities.BaseClass import BaseClass


class TestManageProfile(BaseClass) :

    file_path = "../data/test_data.json"
    with open(file_path) as f :
        test_data = json.load(f)
        test_list = test_data["data"]

    @pytest.mark.parametrize("test_list_item", test_list)
    def test_manage_profile(self, test_list_item):

        login_page = LoginPage(self.driver) #LoginPage class object
        login_page.open_signin() #Open signin  screen
        login_page.valid_login(test_list_item["validMobile"], test_list_item["validPsw"]) #Login with valid credentials

        manage_profile = ManageProfile(self.driver) #ManageProfile class object
        manage_profile.validate_user_name_header(test_list_item["loginUserFirstName"]) #Validate username
        manage_profile.open_manage_profile() #Open manage profile
        manage_profile.update_user_details(test_list_item["userFullName"], test_list_item["userProfileImagePath"]) #Update the user details
