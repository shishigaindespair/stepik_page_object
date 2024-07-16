from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        # email = str(time.time()) + "@fakemail.org"
        # password = str(time.time())
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Ссылка должна содержать слово login"  # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Форма логина не найдена"  # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Форма регистрации не найдена"  # реализуйте проверку, что есть форма регистрации на странице
