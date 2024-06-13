from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "H1")
    CONFIRM_MSG = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//article[@class='product_page']//p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p[contains(text(), 'Стоимость')]/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
