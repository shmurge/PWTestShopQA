import allure

from config.links import Links
from elements.base_element import BaseElement
from pages.header_page import HeaderPage
from locators.locs_account_page import AccountPageLocators


class AccountPage(HeaderPage):
    PAGE_URL = Links.ACCOUNT_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.my_account_header = BaseElement(
            page=self.page, name='Мой аккаунт', selector=AccountPageLocators.MY_ACCOUNT_HEADER
        )
        self.username_in_account = BaseElement(
            page=self.page, name='Имя пользователя', selector=AccountPageLocators.USERNAME
        )
        self.user_email_in_account = BaseElement(
            page=self.page, name='Email', selector=AccountPageLocators.USER_EMAIL)

    def user_information_is_correct(self, username, user_email):
        with allure.step('Информация о пользователе корректна'):
            self.my_account_header_is_displayed()
            self.check_username(username)
            self.check_user_email(user_email)

    def my_account_header_is_displayed(self):
        self.expect.elt_to_be_visible(
            element=self.my_account_header.find_element(),
            element_name=self.my_account_header.name
        )

    def check_username(self, exp):
        with allure.step(f'{self.username_in_account.name} в профиле корректное'):
            self.expect.elt_to_have_text(
                element=self.username_in_account.find_element(),
                element_name=self.username_in_account.name,
                exp_text=exp
            )

    def check_user_email(self, exp):
        with allure.step(f'{self.user_email_in_account.name} в профиле корректный'):
            self.expect.elt_to_have_text(
                element=self.user_email_in_account.find_element(),
                element_name=self.user_email_in_account.name,
                exp_text=exp
            )
