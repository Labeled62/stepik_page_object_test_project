from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_EDIT = (By.CSS_SELECTOR, "#id_registration-email")  # поле ввода email для регистрации
    PASS_EDIT = (By.CSS_SELECTOR, "#id_registration-password1")  # поле ввода пароля для регистрации
    PASS_SECOND_EDIT = (By.CSS_SELECTOR, "#id_registration-password2")  # поле повторите пароль
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")  # кнопка зарегестрироваться
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in") #сообщение об успешной регистрации

class ProductPageLocators:
    BTN_ADD_TO_BUCKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")  # кнопка добавления в корзину
    ADD_TO_BASKET_WINDOW = (
        By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in")  # окно об успешном добавлении в корзину
    PRODUCT_NAME = (By.TAG_NAME, "h1")  # название продукта
    ADD_TO_BASKET_PRODUCT_NAME = (
        By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")  # название товара добавленного в корзину
    PRICE_MESSAGE_WINDOW = (
        By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in")  # окно с суммой в корзине (ценой)
    PRICE_VALUE_IN_MESSAGE = (By.CSS_SELECTOR,
                              "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child("
                              "1) > strong")  # цена в сообщение о добавлении
    PRICE_VALUE = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")  # цена товара


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span > a") #кнопка перехода в корзину (находится здесь, т.к. висит в шапке)
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")  # в корзине есть итемы
    EMPTY_BASKET = (By.CSS_SELECTOR,
                    "#content_inner > p")  # здесь хранится сообщение о пустоте корзины, к тексту не подсасываюсь, вредно
