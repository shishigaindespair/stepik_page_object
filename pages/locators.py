from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_TEXT = (By.XPATH, "//div[@class='content']//p[contains(text(), 'корзина пуста')]")
    GOODS_LIST = (By.CLASS_NAME, "basket-title")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PASS_FIELD1 = (By.NAME, "registration-password1")
    REGISTER_PASS_FIELD2 = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "H1")
    CONFIRM_MSG = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//article[@class='product_page']//p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p[contains(text(), 'Стоимость')]/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
