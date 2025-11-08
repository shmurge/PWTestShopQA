from playwright.sync_api import Page, Locator


class BaseElement:

    def __init__(self, page: Page, name, selector):
        self.page = page
        self.name = name
        self.selector = selector
        self.timeout = 30000

    def find_element(self) -> Locator:
        return self.page.locator(self.selector)

    # def find_elements(self):
    #     return self.page.locator(self.selector).element_handles()

    def find_elements(self):
        return self.page.locator(self.selector).all()

    def click(self, element=None):
        element = element if element else self.find_element()
        element.click()

    def is_visible(self, element=None):
        element = element if element else self.find_element()
        try:
            element.is_visible(timeout=self.timeout)
        except TimeoutError:
            return False

        return True

    def wait_for_visible(self, element=None):
        element = element if element else self.find_element()
        element.wait_for(timeout=self.timeout, state='visible')

    # def get_element(self):
    #     try:
    #         self.wait.until(EC.visibility_of_element_located(self.locator))
    #         return self.browser.find_element(*self.locator)
    #     except TimeoutException:
    #         f'Элемент {self.name} не найден!'
    #
    # def get_elements(self):
    #     self.wait.until(EC.visibility_of_element_located(self.locator))
    #     return self.browser.find_elements(*self.locator)
    #
    # def find_element_by_text(self, text):
    #     self.wait.until(EC.visibility_of_element_located(('xpath', f"//*[text()='{text}']")))
    #     element = self.browser.find_element('xpath', f"//*[text()='{text}']")
    #
    #     return element
    #
    # def select_element_by_text(self, text):
    #     self.wait.until(EC.visibility_of_element_located(('xpath', f"//*[text()='{text}']")))
    #     element = self.browser.find_element('xpath', f"//*[text()='{text}']")
    #     self.wait.until(EC.element_to_be_clickable(element))
    #     element.click()
    #
    # def click(self, element=None):
    #     element = element if element else self.get_element()
    #     self.wait.until(EC.element_to_be_clickable(element))
    #     element.click()
    #
    # def double_click(self, element=None):
    #     element = element if element else self.get_element()
    #     self.wait.until(EC.element_to_be_clickable(element))
    #     self.action.double_click(element).perform()
    #
    # def submit(self, element=None):
    #     element = element if element else self.get_element()
    #     element.submit()
    #
    # def scroll_to_element(self, element=None):
    #     element = element if element else self.get_element()
    #     self.browser.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element
    #     )
    #
    def move_to_element(self, element=None):
        element = element if element else self.find_element()
        element.hover()

    def get_text_of_element(self, element=None):
        element = element if element else self.find_element()
        return element.text_content().strip()

    # def is_visible(self, timeout=15, frequency=1, element=None):
    #     element = element if element else self.locator
    #     self.wait = WebDriverWait(self.browser, timeout, frequency)
    #     try:
    #         self.wait.until(EC.visibility_of_element_located(element))
    #     except TimeoutException:
    #         return False
    #     return True
    #
    # def is_not_visible(self, timeout=1, frequency=0.5, element=None):
    #     element = element if element else self.locator
    #     self.wait = WebDriverWait(self.browser, timeout, frequency)
    #     try:
    #         self.wait.until(EC.invisibility_of_element_located(element))
    #     except TimeoutException:
    #         return False
    #     return True
    #
    # def is_present(self, timeout=15, frequency=1, element=None):
    #     element = element if element else self.locator
    #     self.wait = WebDriverWait(self.browser, timeout, frequency)
    #     try:
    #         self.wait.until(EC.presence_of_element_located(element))
    #     except TimeoutException:
    #         return False
    #     return True
    #
    # def is_displayed(self, element=None):
    #     element = element if element else self.get_element()
    #
    #     return element.is_displayed()
    #
    # def is_selected(self, element=None):
    #     element = element if element else self.get_element()
    #
    #     return element.is_selected()
    #
    # def get_attribute(self, attribute, element=None):
    #     element = element if element else self.get_element()
    #
    #     return element.get_attribute(attribute)
