import os

import pytest
import allure
from dotenv import load_dotenv
from playwright.sync_api import Page, BrowserContext

from config.links import Links
# from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
# from pages.main_page import MainPage
# from pages.product_page import ProductPage


# @pytest.fixture()
# def pre_login(browser):
#     load_dotenv()
#
#     page = LoginPage(browser)
#     page.open()
#     page.fill_login_form(
#         login=os.getenv('LOGIN'),
#         password=os.getenv('PASSWORD')
#     )
#     page = AccountPage(browser)
#
#     page.user_information_is_correct(
#         username=os.getenv('USERNAME'),
#         user_email=os.getenv('LOGIN')
#     )


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})

    return page

# @pytest.fixture()
# def pre_goto_prod_page(browser):
#     page = MainPage(browser)
#     page.open()
#     page.is_opened()
#     page.select_random_product()


# @pytest.fixture()
# def pre_add_random_product_to_cart(browser):
#     page = MainPage(browser)
#     page.open()
#     page.is_opened()
#     page.select_random_product()
#
#     page = ProductPage(browser)
#     page.add_prod_to_cart_and_continue_shopping()
#
#     page = HeaderPage(browser)
#     page.check_prods_quantity_in_header(exp=1)
#
#
# @pytest.fixture()
# def pre_add_several_random_products_to_cart(browser):
#     page = ProductPage(browser)
#     page.add_multiple_prod_to_cart()
#
#
# @pytest.fixture()
# def pre_go_to_customize_desk_page(browser):
#     page = MainPage(browser)
#     page.open(Links.CUSTOMIZE_DESK_PAGE)
