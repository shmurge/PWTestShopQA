import allure

from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from pages.header_page import HeaderPage
from locators.locs_login_page import LoginPageLocators


class LoginPage(HeaderPage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.login_form = BaseElement(page=self.page, name='Форма авторизации', selector=LoginPageLocators.LOGIN_FORM)
        self.email_input = Input(page=self.page, name='Email', selector=LoginPageLocators.EMAIL_INPUT)
        self.password_input = Input(page=self.page, name='Пароль', selector=LoginPageLocators.PASSWORD_INPUT)
        self.login_button = Button(page=self.page, name='Войти', selector=LoginPageLocators.LOGIN_BUTTON)
        self.create_account_link = Button(
            page=self.page, name='Создать аккаунт', selector=LoginPageLocators.CREATE_ACCOUNT_LINK
        )
        self.alert = BaseElement(page=self.page, name='Алерт', selector=LoginPageLocators.ALERT)

    def login_form_is_displayed(self):
        with allure.step(f'{self.login_form.name} отображается'):
            self.expect(
                self.login_form.find_element(),
                self.attach_screenshot(self.login_form.name)
            )

    def go_to_create_account_page(self):
        with allure.step('Перейти на страницу создания аккаунта'):
            self.create_account_link.click()

    def fill_email_input(self, email):
        with allure.step(f'Заполнить {self.email_input.name}'):
            self.email_input.fill_input(email)

    def fill_password_input(self, password):
        with allure.step(f'Заполнить {self.password_input.name}'):
            self.password_input.fill_input(password)

    def click_on_login_button(self):
        with allure.step(f'Кликнуть по {self.login_button.name}'):
            self.login_button.click()

    def fill_login_form(self, login, password):
        with allure.step(f'Заполнить {self.login_form.name}'):
            self.fill_email_input(login)
            self.fill_password_input(password)
            self.click_on_login_button()

    def should_be_correct_placeholders_in_login_form(self, exp_email_placeholder, exp_password_placeholder):
        with allure.step(f'Проверить плэйсхолдеры в {self.login_form.name}'):
            self.expect(
                self.email_input.find_element(),
                self.attach_screenshot(self.email_input.name)
            ).to_have_attribute(
                name='placeholder',
                value=exp_email_placeholder
            )
            self.expect(
                self.password_input.find_element(),
                self.attach_screenshot(self.password_input.name)
            ).to_have_attribute(
                name='placeholder',
                value=exp_password_placeholder)

    def error_alert_is_displayed(self, exp_alert):
        with allure.step(f'{self.alert.name} отображается'):
            self.expect(
                self.alert.find_element(),
                self.attach_screenshot(self.alert.name)
            ).to_have_text(expected=exp_alert)
