from playwright.sync_api import Page, expect
from utils.utils import Utils


class ExpectsAndAsserts:

    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000
        self.utils = Utils(self.page)

    def elt_to_be_visible(
            self,
            element,
            element_name,
            timeout=None
    ):
        timeout = timeout if timeout else self.timeout
        try:
            expect(
                actual=element,
                message=f'{element_name} не отображается!'
            ).to_be_visible(timeout=timeout)
        except AssertionError:
            self.utils.attach_screenshot(element_name)
            raise

    def elt_to_be_hidden(
            self,
            element,
            element_name,
            timeout=None
    ):
        timeout = timeout if timeout else self.timeout
        try:
            expect(
                actual=element,
                message=f'{element_name} не должен отображаться!'
            ).to_be_hidden(timeout=timeout)
        except AssertionError:
            self.utils.attach_screenshot(element_name)
            raise

    def elt_to_have_text(
            self,
            element,
            element_name,
            exp_text
    ):
        try:
            expect(
                actual=element,
                message=f'Некорректный текст в {element_name}!'
            ).to_have_text(expected=exp_text, timeout=self.timeout)
        except AssertionError:
            self.utils.attach_screenshot(element_name)
            raise

    def elt_to_have_attribute(
            self,
            element,
            element_name,
            assert_message,
            exp_attr_name,
            exp_attr_value
    ):
        try:
            expect(
                actual=element,
                message=assert_message
            ).to_have_attribute(name=exp_attr_name, value=exp_attr_value, timeout=self.timeout)
        except AssertionError:
            self.utils.attach_screenshot(element_name)
            raise

    def page_to_have_url(
            self,
            exp_url
    ):
        try:
            expect(
                actual=self.page,
                message=f'Некорректный url на странице!'
            ).to_have_url(url_or_reg_exp=exp_url, timeout=self.timeout)
        except AssertionError:
            self.utils.attach_screenshot(screenshot_name='Page url')
            raise

    def input_to_have_value(
            self,
            element,
            element_name,
            exp_value
    ):
        try:
            expect(
                actual=element,
                message=f'Некорректное значение в {element_name}!'
            ).to_have_value(value=exp_value)
        except AssertionError:
            self.utils.attach_screenshot(element_name)
            raise

    def assert_data_equal_data(self, act_res, exp_res, message):
        assert act_res == exp_res, (f'{message}!\n'
                                    f'ОР: {exp_res}\n'
                                    f'ФР: {act_res}\n'
                                    f'{self.utils.attach_screenshot(screenshot_name="Screenshot")} прикреплен')

    def assert_data_in_data(self, act_res, exp_res, message):
        assert act_res in exp_res, (f'{message}!\n'
                                    f'{self.utils.attach_screenshot(screenshot_name="Screenshot")} прикреплен')

    def assert_data_not_in_data(self, act_res, exp_res, message):
        assert act_res not in exp_res, (f'{message}!\n'
                                        f'{self.utils.attach_screenshot(screenshot_name="Screenshot")} прикреплен')