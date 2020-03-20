from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_is_not_present_on_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "PRODUCT IN BASKET"

    def should_be_text_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "BASKET NOT EMPTY!!!"


