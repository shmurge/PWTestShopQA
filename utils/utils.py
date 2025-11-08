import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page


class Utils:

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Прикрепить скриншот')
    def attach_screenshot(self, screenshot_name):
        allure.attach(
            body=self.page.screenshot(full_page=True),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

        return screenshot_name
