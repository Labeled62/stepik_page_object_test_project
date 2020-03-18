from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    BTN_ADD_TO_BUCKET=(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADD_TO_BASKET_WINDOW = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_MESSAGE_WINDOW = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_VALUE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_VALUE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")



