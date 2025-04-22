import json

import pytest

from Pages.ItemOrder import ItemOrder
from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass

class TestItemOrder(BaseClass) :

    file_path = "../data/test_data.json"
    with open(file_path) as f :
        test_data = json.load(f)
        test_list = test_data["data"]

    @pytest.mark.parametrize("test_list_item", test_list)
    def test_item_order(self, test_list_item):

        login_page = LoginPage(self.driver) #LoginPage class object
        login_page.open_signin() #Open signin  screen
        login_page.valid_login(test_list_item["validMobile"], test_list_item["validPsw"]) #Login with valid credentials

        item_order = ItemOrder(self.driver) #ItemOrder page class object
        item_order.search_item(test_list_item["searchItemName"]) #Search the item
        item_order.add_item_to_cart(test_list_item["actualItemName"], test_list_item["actualItemPrice"]) #Add the item into cart
        item_order.open_cart() #Open the cart screen
        item_order.validate_item_data(test_list_item["actualItemName"], test_list_item["actualItemPrice"]) #Validate the item data into cart