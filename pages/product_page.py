from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
import time

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def bucket_button_click(self):
        add_to_bskt_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BUCKET)
        add_to_bskt_btn.click()

    def should_be_product_page(self):
        self.solve_quiz_and_get_code()
        self.should_be_add_to_basket_button()
        self.should_be_message_add_to_basket()
        self.should_be_product_name_valid()
        self.should_be_product_value_valid()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BUCKET), "This button not on page"

    def should_be_message_add_to_basket(self):
        print('start-test')
        #time.sleep()
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_WINDOW), "ADD TO BASKET WINDOWS OUT OF PAGE"

    def should_be_product_name_valid(self):
        print('name_valid')
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "PRODUCT NAME OUT OF PAGE"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_PRODUCT_NAME), "ADD TO BASKET PRODUCT NAME OUT OF PAGE"
        product_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        #product_text = product_text.text
        add_to_basket_product_name = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_PRODUCT_NAME).text
        #add_to_basket_product_name = add_to_basket_product_name
        print(product_text)
        print(add_to_basket_product_name)
        assert product_text == add_to_basket_product_name, "ADDED PRODUCT != PRODUCT ON CARD"

    def should_be_product_value_valid(self):
        print('value_valid')
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE_WINDOW), "PRICE MESSAGE OUT OF PAGE!"
        assert self.is_element_present(*ProductPageLocators.PRICE_VALUE_IN_MESSAGE), "PRICE VALUE IN MESSAGE OUT OF PAGE"
        assert self.is_element_present(*ProductPageLocators.PRICE_VALUE), "PRICE VALUE OUT OF PAGE"
        value_in_message_text = self.browser.find_element(*ProductPageLocators.PRICE_VALUE_IN_MESSAGE).text
        #value_in_message_text = value_in_message_text
        value_text = self.browser.find_element(*ProductPageLocators.PRICE_VALUE).text
        #value_text = value_text
        assert value_in_message_text == value_text, "PRICE IN MESSAGE != PRICE ON PAGE"