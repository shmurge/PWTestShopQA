import allure

from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_header_page import HeaderPageLocators
from pages.base_page import BasePage

from time import sleep

class HeaderPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.main_logo = BaseElement(
            page=self.page, name='Лого', selector=HeaderPageLocators.MAIN_LOGO
        )
        self.cart_button = Button(
            page=self.page, name='Корзина', selector=HeaderPageLocators.LINK_CART
        )
        self.counter_on_cart = BaseElement(
            page=self.page, name='Кол-во товаров в корзине', selector=HeaderPageLocators.COUNTER_ON_CART
        )
        self.main_search_button = Button(
            page=self.page, name='Главный поиск', selector=HeaderPageLocators.BUTTON_MAIN_SEARCH
        )
        self.sign_in_button = Button(
            page=self.page, name='Войти', selector=HeaderPageLocators.LINK_SIGN_IN
        )
        self.username_in_header = BaseElement(
            page=self.page, name='Имя пользователя', selector=HeaderPageLocators.USERNAME
        )
        self.my_account_button = Button(
            page=self.page, name='Мой аккаунт', selector=HeaderPageLocators.MY_ACCOUNT_BUTTON
        )
        self.logout_button = Button(
            page=self.page, name='Выйти', selector=HeaderPageLocators.LOGOUT_BUTTON)

    def goto_main_page(self):
        with allure.step('Перейти на главную страницу'):
            self.main_logo.click()

    def goto_login_page(self):
        with allure.step('Перейти на страницу логина'):
            self.sign_in_button.click()

    def goto_cart_page(self):
        with allure.step('Перейти на страницу корзины'):
            self.cart_button.click()

    def open_main_search(self):
        with allure.step('Открыть главный поиск'):
            self.main_search_button.click()

    def username_is_correct(self, exp):
        with allure.step(f'{self.username_in_header.name} в хэдере корректное'):
            self.expect.elt_to_have_text(
                element=self.username_in_header.find_element(),
                element_name=self.username_in_header.name,
                exp_text=exp
            )

    def goto_my_account(self):
        with allure.step('Перейти в аккаунт'):
            self.username_in_header.move_to_element()
            self.my_account_button.click()

    def logout(self):
        with allure.step('Выход из аккаунта'):
            self.username_in_header.move_to_element()
            self.logout_button.click()

    def sign_in_button_is_displayed(self):
        with allure.step(f'{self.sign_in_button.name} отображается'):
            self.expect.elt_to_be_visible(
                element=self.sign_in_button.find_element(),
                element_name=self.sign_in_button.name
            )

    #
    # def check_prods_quantity_in_header(self, exp: int):
    #     with allure.step('Проверить количество товаров в счетчике хэдера'):
    #         act = int(self.counter_on_cart.get_text_of_element())
    #
    #         assert self.wait.until(
    #             self.ec.text_to_be_present_in_element(self.counter_on_cart.locator, str(exp))
    #         ), (f'Некорректное количество товаров в счетчике хэдера\n'
    #             f'ОР: {exp}\n'
    #             f'ФР: {act}')
