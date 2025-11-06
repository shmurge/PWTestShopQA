import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def open(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Открыть страницу: {page_url}'):
            self.page.goto(page_url)

    def is_opened(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Страница {page_url} открыта'):
            self.expect(self.page).to_have_url(page_url)

    @allure.step('Прикрепить скриншот')
    def attach_screenshot(self, screenshot_name):
        allure.attach(
            body=self.page.screenshot(full_page=True),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

        return screenshot_name

    def assert_data_equal_data(self, act_res, exp_res, message):
        assert act_res == exp_res, (f'{message}!\n'
                                    f'ОР: {exp_res}\n'
                                    f'ФР: {act_res}\n'
                                    f'{self.attach_screenshot("Screenshot")} прикреплен')

    def assert_data_in_data(self, act_res, exp_res, message):
        assert act_res in exp_res, (f'{message}!\n'
                                    f'{self.attach_screenshot("Screenshot")} прикреплен')

    def assert_data_not_in_data(self, act_res, exp_res, message):
        assert act_res not in exp_res, (f'{message}!\n'
                                        f'{self.attach_screenshot("Screenshot")} прикреплен')
