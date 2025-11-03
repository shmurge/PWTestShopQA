import allure
from playwright.sync_api import expect

from config.links import Links
from elements.base_element import BaseElement
from locators.locs_account_page import AccountPageLocators
from pages.header_page import HeaderPage


class AccountPage(HeaderPage):
    PAGE_URL = Links.ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.my_account_header = BaseElement(
            page=self.page, name='Мой аккаунт', selector=AccountPageLocators.MY_ACCOUNT_HEADER
        )
        self.username_in_account = BaseElement(
            page=self.page, name='Имя пользователя', selector=AccountPageLocators.USERNAME
        )
        self.user_email_in_account = BaseElement(
            page=self.page, name='Email', selector=AccountPageLocators.USER_EMAIL)

    def account_page_is_displayed(self):
        with allure.step(f'Отображается {self.my_account_header.name}'):
            expect(
                self.my_account_header.find_element(),
                self.attach_screenshot(self.my_account_header.name)
            ).to_be_visible()

    def user_information_is_correct(self, username, user_email):
        with allure.step('Информация о пользователе корректна'):
            self.check_username(username)
            self.check_user_email(user_email)

    def check_username(self, exp):
        with allure.step(f'{self.username_in_account.name} в профиле корректное'):
            expect(
                self.username_in_account.find_element(),
                self.attach_screenshot(self.username_in_account.name)
            ).to_have_text(expected=exp)

    def check_user_email(self, exp):
        with allure.step(f'{self.user_email_in_account.name} в профиле корректный'):
            expect(
                self.user_email_in_account.find_element(),
                self.attach_screenshot(self.user_email_in_account.name)
            ).to_have_text(expected=exp)
