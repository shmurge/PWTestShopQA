import re

import allure

from elements.input import Input
from elements.base_element import BaseElement
from elements.button import Button
from locators.locs_modal_add_to_cart import ModalAddToCartLocators
from pages.base_page import BasePage


class ModalAddToCart(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.add_to_cart_modal = BaseElement(
            page=self.page, name='Модалка "Добавить в корзину"', selector=ModalAddToCartLocators.ADD_TO_CART_MODAL
        )
        self.proceed_to_checkout_button = Button(
            page=self.page, name='Перейти к оформлению', selector=ModalAddToCartLocators.PROCEED_TO_CHECKOUT_BUTTON
        )
        self.continue_shopping_button = Button(
            page=self.page, name='Продолжить покупки', selector=ModalAddToCartLocators.CONTINUE_SHOPPING_BUTTON
        )
        self.close_modal_button = Button(
            page=self.page, name='Закрыть модалку', selector=ModalAddToCartLocators.CLOSE_ADD_TO_CART_MODAL_BUTTON
        )
        self.product_title_on_modal = BaseElement(
            page=self.page, name='Наименование товара в модалке', selector=ModalAddToCartLocators.PRODUCT_TITLE
        )
        self.product_price_on_modal = BaseElement(
            page=self.page, name='Стоимость товара в модалке', selector=ModalAddToCartLocators.PRODUCT_PRICE
        )
        self.product_total_price_on_modal = BaseElement(
            page=self.page, name='Итоговая стоимость в модалке', selector=ModalAddToCartLocators.TOTAL_PRICE
        )
        self.add_one_unit_button = Button(
            page=self.page, name='Добавить одну единицу товара в модалке',
            selector=ModalAddToCartLocators.ADD_ONE_BUTTON
        )
        self.remove_one_unit_button = Button(
            page=self.page, name='Удалить одну единицу товара в модалке',
            selector=ModalAddToCartLocators.REMOVE_ONE_BUTTON
        )
        self.units_quantity_input = Input(
            page=self.page, name='Счетчик единиц товара в модалке', selector=ModalAddToCartLocators.QUANTITY_INPUT
        )

    def close_modal(self):
        with allure.step(f'Закрыть {self.add_to_cart_modal.name}'):
            self.close_modal_button.click()

    def modal_should_not_be_displayed(self):
        with allure.step(f'{self.add_to_cart_modal.name} не отображается!'):
            self.expect.elt_to_be_hidden(
                element=self.add_to_cart_modal.find_element(),
                element_name=self.add_to_cart_modal.name,
                timeout=2000
            )

    def check_prod_title_price_and_quantity(self, exp_title, exp_price, exp_quan):
        with allure.step('Проверить наименование, стоимость и количество товаров в модалке'):
            self.check_product_title(exp_title)
            self.check_product_price(exp_price)
            self.check_product_units_quantity(exp_quan)

    def check_product_title(self, exp, full_match=False):
        with allure.step(f'Проверить {self.product_title_on_modal.name}'):
            title_in_modal = self.product_title_on_modal.get_text_of_element()
            if full_match:
                self.expect.elt_to_have_text(
                    element=self.product_title_on_modal.find_element(),
                    element_name=self.product_title_on_modal.name,
                    exp_text=exp
                )
                # self.assert_data_equal_data(
                #     act_res=title_in_modal,
                #     exp_res=exp,
                #     message=f'Некорректное {self.product_title_on_modal.name}'
                # )
            else:
                self.expect.elt_to_have_text(
                    element=self.product_title_on_modal.find_element(),
                    element_name=self.product_title_on_modal.name,
                    exp_text=re.compile(exp)
                )
                # self.assert_data_in_data(
                #     act_res=exp,
                #     exp_res=title_in_modal,
                #     message=f'{self.product_title_on_modal} не содержит {exp}'
                # )

    def check_product_price(self, exp):
        with allure.step(f'Проверить {self.product_price_on_modal.name}'):
            self.expect.elt_to_have_text(
                element=self.product_price_on_modal.find_element(),
                element_name=self.product_price_on_modal.name,
                exp_text=exp
            )
            # act = self.product_price_on_modal.get_text_of_element()
            #
            # self.assert_data_equal_data(
            #     act_res=act,
            #     exp_res=exp,
            #     message=f'Некорректная {self.product_price_on_modal.name}'
            # )

    def check_product_units_quantity(self, exp):
        with allure.step('Проверить количество единиц товара'):
            self.expect.input_to_have_value(
                element=self.units_quantity_input.find_element(),
                element_name=self.units_quantity_input.name,
                exp_value=str(exp)
            )
            # self.expect.elt_to_have_attribute(
            #     element=self.units_quantity_input.find_element(),
            #     element_name=self.units_quantity_input.name,
            #     assert_message=f'Некорректное значение в {self.units_quantity_input.name}!',
            #     exp_attr_name='value',
            #     exp_attr_value=str(exp)
            #)
            # act = self.get_prod_units_quantity_on_modal()

            # self.assert_data_equal_data(
            #     act_res=act,
            #     exp_res=exp,
            #     message='Некорректное количество единиц товара'
            # )

    def check_product_total_price(self, exp):
        with allure.step(f'Проверить {self.product_total_price_on_modal.name}'):
            self.expect.elt_to_have_text(
                element=self.product_total_price_on_modal.find_element(),
                element_name=self.product_total_price_on_modal.name,
                exp_text=exp
            )
            # act = self.product_total_price_on_modal.get_text_of_element()
            #
            # self.assert_data_equal_data(
            #     act_res=act,
            #     exp_res=exp,
            #     message=f'Некорректная {self.product_total_price_on_modal.name}'
            # )

    # def get_prod_units_quantity_on_modal(self):
    #     return int(self.units_quantity_input.get_attribute('value'))
