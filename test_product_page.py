from pages.base_page import BasePage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_and_check()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
# def test_guest_cant_see_success_message(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.message_should_disappear_after_adding_product_to_basket()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
