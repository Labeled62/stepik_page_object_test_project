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
        self.bucket_button_click()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(10)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(1500)
        except NoAlertPresentException:
            print("No second alert presented")
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BUCKET), "This button not on page"
    def should_be_message_add_to_basket(selfs):
        assert

