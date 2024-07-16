from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_and_check(self):
        self.add_to_basket()
        # self.solve_quiz_and_get_code()
        self.should_be_correct_product()
        self.should_be_correct_price()

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def should_be_correct_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        confirm_msg = self.browser.find_element(*ProductPageLocators.CONFIRM_MSG).text
        assert product_name == confirm_msg, "Похоже, в корзину добавлен другой товар"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Похоже, цена не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
