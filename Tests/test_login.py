import json

import pytest

from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestLogin(BaseClass) :

    file_path = "../data/test_data.json"
    with open(file_path) as f :
        test_data = json.load(f)
        test_list = test_data["data"]

    @pytest.mark.parametrize("test_list_item", test_list)
    def test_login(self, test_list_item):

        login_page = LoginPage(self.driver) #LoginPage class object
        login_page.open_signin() #Open signin  screen
        login_page.invalid_mobile(test_list_item["invalidMobile"]) #Signin with invalid mobile number
        login_page.invalid_password(test_list_item["validMobile"], test_list_item["invalidPsw"]) #Signin with invalid password
        login_page.valid_password(test_list_item["validPsw"]) #Signin with valid password
