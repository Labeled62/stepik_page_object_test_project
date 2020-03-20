from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, BasketPageLocators
from .login_page import LoginPage
from .basket_page import BasketPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):  # ПРАВОСЛАВИЕ ИЛИ ЗАГЛУШКИ!!111
        super(MainPage, self).__init__(*args, **kwargs)


