from playwright.sync_api import Page, Locator, TimeoutError


class BaseElement:

    def __init__(self, page: Page, name, selector):
        self.page = page
        self.name = name
        self.selector = selector
        self.timeout = 30000

    def find_element(self) -> Locator:
        return self.page.locator(self.selector)

    def find_elements(self):
        return self.page.locator(self.selector).all()

    def click(self, element=None):
        element = element if element else self.find_element()
        element.click()

    def is_visible(self, element=None, timeout=None):
        element = element if element else self.find_element()
        timeout = timeout if timeout else self.timeout
        try:
            element.wait_for(state='visible', timeout=timeout)
        except TimeoutError:
            return False

        return True

    def wait_for_visible(self, element=None, multiple=False):
        element = element if element else self.find_element()
        if multiple:
            cnt = element.count()
            for i in range(cnt):
                element.nth(i).wait_for(timeout=self.timeout, state='visible')
        element.wait_for(timeout=self.timeout, state='visible')

    def wait_for_hidden(self, element=None, multiple=False):
        element = element if element else self.find_element()
        if multiple:
            cnt = element.count()
            for i in range(cnt):
                element.nth(i).wait_for(timeout=self.timeout, state='hidden')
        element.wait_for(timeout=self.timeout, state='hidden')

    def move_to_element(self, element=None):
        element = element if element else self.find_element()
        element.hover()

    def get_text_of_element(self, element=None) -> str:
        element = element if element else self.find_element()
        text = element.text_content().strip()
        text = text.replace('\u00A0', ' ')

        return text

    def get_inner_text_list(self) -> list:

        return [t.inner_text().replace('\u00A0', ' ').strip() for t in self.find_elements()]

    def get_attribute(self, attribute, element=None):
        element = element if element else self.find_element()

        return element.get_attribute(name=attribute, timeout=self.timeout)
