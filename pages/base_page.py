import allure
from playwright.sync_api import Page
from expects_and_asserts.expects_and_asserts import ExpectsAndAsserts


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.expect = ExpectsAndAsserts(self.page)

    def open(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Открыть страницу: {page_url}'):
            self.page.goto(page_url)

    def is_opened(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Страница {page_url} открыта'):
            self.expect.page_to_have_url(
                exp_url=self.PAGE_URL
            )
