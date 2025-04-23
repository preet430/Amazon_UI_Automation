import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ItemOrder :

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.ID, "twotabsearchtextbox")
    suggested_item_name = (By.XPATH, "//span[normalize-space()='gb']")

    #Search the item & click on it
    def search_item(self, item_name):
        self.driver.find_element(*ItemOrder.search_box).click()
        time.sleep(3)
        self.driver.find_element(*ItemOrder.search_box).send_keys(item_name)
        self.driver.implicitly_wait(3)
        self.driver.find_element(*ItemOrder.suggested_item_name).click()

    mobile_ele = (By.XPATH, "//h2[@aria-label='Apple iPhone 15 (128 GB) - Black']//span[contains(text(),'Apple iPhone 15 (128 GB) - Black')]")
    add_cart_btn = (By.XPATH, "//button[@id='a-autoid-3-announce']")
    plus_icon = (By.XPATH, "//span[@class='a-icon a-icon-small-add']")
    mobile_price = (By.XPATH, "//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_3']"
                              "//span[@class='a-price-whole'][normalize-space()='61,390']")

    #Add the item into cart
    def add_item_to_cart(self, mob_name, mob_price):
        mobile = self.driver.find_element(*ItemOrder.mobile_ele)
        mobile_text = self.driver.find_element(*ItemOrder.mobile_ele).text
        # print("Mobile Name:", mobile_text)
        actions = ActionChains(self.driver)
        actions.move_to_element(mobile).perform()
        assert mobile_text in mob_name
        price_text = self.driver.find_element(*ItemOrder.mobile_price).text
        assert price_text in mob_price
        self.driver.find_element(*ItemOrder.add_cart_btn).click()
        time.sleep(3)
        self.driver.find_element(*ItemOrder.plus_icon).click()
        time.sleep(3)

    cart_btn = (By.CSS_SELECTOR, "#nav-cart-count")

    #Open the cart screen
    def open_cart(self):
        self.driver.find_element(*ItemOrder.cart_btn).click()

    cart_mob_name = (By.XPATH, "//span[@class='a-truncate-cut']")
    cart_mob_price = (By.XPATH, "//span[@class='a-price']//span[@class='a-price-whole']")
    cart_subtotal = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap'][contains(text(),'₹1,22,780.00')]")
    delete_btn = (By.XPATH, "//input[@data-feature-id='item-delete-button']")

    #Validate item data in cart & remove the item
    def validate_item_data(self, cart_mobile_name, cart_mobile_price):
        cart_mob_text = self.driver.find_element(*ItemOrder.cart_mob_name).text
        assert cart_mob_text in cart_mobile_name
        cart_mob_price_text = self.driver.find_element(*ItemOrder.cart_mob_price).text
        assert cart_mob_price_text in cart_mobile_price
        price_cleaned = int(cart_mob_price_text.replace(',', ''))
        cart_subtotal_text = self.driver.find_element(*ItemOrder.cart_subtotal).text
        subtotal_cleaned = int(float(cart_subtotal_text.replace('₹', '').replace(',', '').strip()))
        expected_subtotal = price_cleaned * 2
        assert expected_subtotal == subtotal_cleaned
        self.driver.find_element(*ItemOrder.delete_btn).click()
        self.driver.implicitly_wait(5)






