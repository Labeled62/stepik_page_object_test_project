from selenium.webdriver.support import expected_conditions as EC
import random
import pytest
from selenium import webdriver
import time
import math

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageLocators, BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # def __init__(self, browser, url, timeout=10):
    # self.browser = browser
    #  self.url = url
    # self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what,
                               timeout=4):  # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):  # будет ждать до тех пор, пока элемент не исчезнет.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self): #переход на страницу логина
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self): #проверки наличия ссылки логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self): #переход в корзитну
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        basket_button.click()

    def should_be_authorized_user(self): #проверка того, что юхер авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
