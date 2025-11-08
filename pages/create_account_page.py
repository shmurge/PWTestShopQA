import os

import allure
from dotenv import load_dotenv, set_key

from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_create_account_page import CreateAccountPageLocators
from pages.header_page import HeaderPage


class CreateAccountPage(HeaderPage):
    PAGE_URL = Links.CREATE_ACCOUNT_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.registration_form = BaseElement(
            page=self.page, name='Форма регистрации', selector=CreateAccountPageLocators.REGISTRATION_FORM
        )
        self.email_input = Input(
            page=self.page, name='Ваш Email', selector=CreateAccountPageLocators.INPUT_LOGIN
        )
        self.username_input = Input(
            page=self.page, name='Ваше имя', selector=CreateAccountPageLocators.INPUT_USERNAME
        )
        self.password_input = Input(
            page=self.page, name='Пароль', selector=CreateAccountPageLocators.INPUT_PASSWORD
        )
        self.password_confirm_input = Input(
            page=self.page, name='Подтверждение пароля', selector=CreateAccountPageLocators.INPUT_PASSWORD_CONFIRM
        )
        self.sign_up_button = Button(
            page=self.page, name='Зарегистрироваться', selector=CreateAccountPageLocators.BUTTON_SUBMIT
        )
        self.alert = BaseElement(
            page=self.page, name='Алерт', selector=CreateAccountPageLocators.ALERT)

    def registration_form_is_displayed(self):
        with allure.step(f'{self.registration_form.name} отображается'):
            self.expect.elt_to_be_visible(
                element=self.registration_form.find_element(),
                element_name=self.registration_form.name
            )

    def fill_email(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.email_input.name}'):
            self.email_input.fill_input(data)
            if save_to_env:
                self.set_env_key('LOGIN', data)

        return data

    def fill_username(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.username_input.name}'):
            self.username_input.fill_input(data)
            if save_to_env:
                self.set_env_key('USERNAME', data)

        return data

    def fill_password(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.password_input.name}'):
            self.password_input.fill_input(data)
            if save_to_env:
                self.set_env_key('PASSWORD', data)

        return data

    def fill_password_confirm(self, data):
        with allure.step(f'Заполнить {self.password_confirm_input.name}'):
            self.password_confirm_input.fill_input(data)

    def click_sign_up(self):
        with allure.step(f'Кликнуть по {self.sign_up_button.name}'):
            self.sign_up_button.click()

    def fill_registration_form(self,
                               email,
                               username,
                               password,
                               save_to_env=True,
                               ):
        with allure.step(f'Заполнить {self.registration_form.name}'):
            self.registration_form.is_visible()
            self.fill_email(email, save_to_env)
            self.fill_username(username, save_to_env)
            self.fill_password(password, save_to_env)
            self.fill_password_confirm(password)
            self.click_sign_up()

    def error_alert_is_displayed(self, exp_alert_text):
        with allure.step(f'{self.alert.name} отображается'):
            with allure.step(f'{self.alert.name} отображается'):
                self.expect.elt_to_be_visible(
                    element=self.alert.find_element(),
                    element_name=self.alert.name
                )
            with allure.step(f'Текст в {self.alert.name} корректный'):
                self.expect.elt_to_have_text(
                    element=self.alert.find_element(),
                    element_name=self.alert.name,
                    exp_text=exp_alert_text
                )

    def check_placeholders_in_registration_form(self, exp):
        with allure.step(f'Проверить плэйсхолдер в {self.username_input.name}'):
            self.expect.elt_to_have_attribute(
                element=self.username_input.find_element(),
                element_name=self.username_input.name,
                assert_message=f'Некорректный плейсхолдер в {self.username_input.name}!',
                exp_attr_name='placeholder',
                exp_attr_value=exp
            )

    @staticmethod
    def set_env_key(key, value):
        load_dotenv('.env')
        os.environ[key] = value
        set_key('.env', key, value)
