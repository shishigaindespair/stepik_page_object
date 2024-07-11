from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_LIST), \
            "The basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "There is no basket-empty alert"



