import random

import allure
from playwright.sync_api import Locator

from config.links import Links
from data_for_tests.data_for_tests import InfoMessage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_main_page import MainPageLocators
from pages.header_page import HeaderPage


class MainPage(HeaderPage):
    PAGE_URL = Links.MAIN_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.search_input = Input(
            page=self.page, name='Поиск', selector=MainPageLocators.SEARCH_INPUT)
        self.searching_result_cnt = BaseElement(
            page=self.page, name='Счетчик найденных товаров', selector=MainPageLocators.SEARCHING_RESULT_CNT
        )
        self.message_no_searching_results = BaseElement(
            page=self.page, name='Сообщение на странице "Ничего не найдено"',
            selector=MainPageLocators.MESSAGE_ON_PAGE_NO_SEARCHING_RESULTS
        )
        self.product_title = Button(
            page=self.page, name='Наименование товара', selector=MainPageLocators.PRODUCT_TITLE
        )
        self.product_price = Button(
            page=self.page, name='Цена товара', selector=MainPageLocators.PRODUCT_PRICE)

    def main_page_is_displayed(self):
        with allure.step('Отображается главная страница'):
            self.expect(
                self.search_input.find_element(),
                self.attach_screenshot(self.search_input.name)
            ).to_be_visible()

    def check_placeholder_in_search_input(self, exp):
        with allure.step(f'Проверить плэйсхолдер в {self.search_input.name}'):
            self.expect(
                self.search_input.find_element(),
                self.attach_screenshot(self.search_input.name)
            ).to_have_attribute(name='placeholder', value=exp)

    def select_random_product(self):
        titles = self.product_title.find_elements()
        prices = self.product_price.find_elements()

        if len(titles) > 1:
            rand_index = random.randrange(0, len(titles))
            t = titles[rand_index].inner_text()
            p = prices[rand_index].inner_text()
            el = titles[rand_index]
        else:
            t = titles[0].inner_text()
            p = prices[0].inner_text()
            el = titles[0]

        with allure.step(f'Выбрать товар: {t}'):
            self.product_title.click(el)

        return t, p

    def search_product(self, data):
        with allure.step(f'Поиск товара: {data}'):
            self.search_input.click()
            self.search_input.fill_autocomplete_input(data)

    def check_searching_result(self, data):
        with allure.step('Проверить результаты поиска товаров'):
            self.found_prods_contain_keyword_in_title(data)
            self.check_result_count()

    def found_prods_contain_keyword_in_title(self, keyword):
        with allure.step(f'Найденные товары содержат {keyword} в наименовании'):
            self.searching_result_cnt.wait_for_visible()
            titles = [t.text_content() for t in self.product_title.find_elements()]

            for title in titles:
                self.assert_data_in_data(
                    act_res=keyword.lower(),
                    exp_res=title.lower(),
                    message=f'Найденный товар {title} не содержит {keyword} в наименовании'
                )

    def check_result_count(self):
        with allure.step('Корректное количество найденных товаров в счетчике'):
            titles = self.product_title.find_elements()
            cnt_res = self.searching_result_cnt.get_text_of_element()
            parenthesis_index = cnt_res.find('(') + 1
            space_index = cnt_res.find(' ')
            res_count = int(cnt_res[parenthesis_index:space_index])

            self.assert_data_equal_data(
                act_res=len(titles),
                exp_res=res_count,
                message='Некорректый результат в счетчике найденных товаров'
            )

    def check_message_with_no_results(self, query):
        with allure.step('Отображается попап с отсутствием результатов поиска'):
            exp = InfoMessage().message_no_results(query)
            try:
                self.expect(
                    self.message_no_searching_results.find_element(),
                    message='Нет модалки с алертом'
                ).to_be_visible()

                self.expect(
                    self.message_no_searching_results.find_element(),
                    message='Модалка с алертом содержит некорректный текст'
                ).to_have_text(expected=exp)
            except AssertionError:
                self.attach_screenshot(self.message_no_searching_results.name)
                raise
