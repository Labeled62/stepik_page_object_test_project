from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random  # для генератора паролей


def pass_gen():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # pass gen
    number = 1
    length = 9
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print(password)
    return password


def email_gen():
    email = str(time.time()) + "@fakemail.org"  # генератор email
    return email


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        login_assert = 'login'
        print(login_url)
        assert login_assert in login_url, "This link is not login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not on page"

    def should_be_register_form(self):
        # форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not on page"

    def register_new_user(self):  # регистрация
        email = email_gen()
        password = pass_gen()
        assert self.is_element_present(*LoginPageLocators.EMAIL_EDIT), "EMAIL_EDIT OUT OF PAGE"
        email_edit1 = self.browser.find_element(*LoginPageLocators.EMAIL_EDIT)
        email_edit1.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASS_EDIT), "PASS_EDIT OUT OF PAGE"
        assert self.is_element_present(*LoginPageLocators.PASS_SECOND_EDIT), "PASS_EDIT2 OUT OF PAGE"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "REGISTRATION BUTTON OUT OF PAGE"
        password_edit1 = self.browser.find_element(*LoginPageLocators.PASS_EDIT)
        password_edit1.send_keys(password)
        password_edit2 = self.browser.find_element(*LoginPageLocators.PASS_SECOND_EDIT)
        password_edit2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_btn.click()
        self.browser.implicitly_wait(5)
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS_MESSAGE), "REGISTER MESSAGE OUT OF PAGE"