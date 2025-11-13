import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import BrowserContext

from config.links import Links
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})

    return page


@pytest.fixture()
def pre_login(page):
    load_dotenv()

    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_login_form(
        login=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD')
    )

    account_page = AccountPage(page)

    account_page.user_information_is_correct(
        username=os.getenv('USERNAME'),
        user_email=os.getenv('LOGIN')
    )


@pytest.fixture()
def pre_goto_prod_page(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.is_opened()
    main_page.select_random_product()


@pytest.fixture()
def pre_add_random_product_to_cart(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.is_opened()
    main_page.select_random_product()

    prod_page = ProductPage(page)
    prod_page.add_prod_to_cart_and_continue_shopping()

    header_page = HeaderPage(page)
    header_page.check_prods_quantity_in_header(exp=1)


@pytest.fixture()
def pre_add_several_random_products_to_cart(page):
    prod_page = ProductPage(page)
    prod_page.add_multiple_prod_to_cart()


@pytest.fixture()
def pre_go_to_customize_desk_page(page):
    main_page = MainPage(page)
    main_page.open(Links.CUSTOMIZE_DESK_PAGE)
