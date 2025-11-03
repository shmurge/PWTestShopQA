from elements.base_element import BaseElement


class Input(BaseElement):

    def __init__(self, page, name, selector):
        super().__init__(page, name, selector)

        self.name = f'Поле: {name}'

    def clear_input(self, element=None):
        element = element if element else self.find_element()
        element.clear()


    def fill_input(self, data, element=None):
        element = element if element else self.find_element()
        element.fill(data)

        return data

    # def fill_autocomplete_input(self, data):
    #     input_1 = self.get_element()
    #     self.wait.until(EC.element_to_be_clickable(self.locator))
    #     self.action.click(input_1)
    #     self.action.send_keys_to_element(input_1, data)
    #     self.action.send_keys_to_element(input_1, Keys.ENTER).perform()
    #
    #     return data
    #
    def get_placeholder(self):
        # return self.get_element().get_attribute('placeholder').strip()
        return self.find_element().get_attribute('placeholder').strip()
    #
    # def press_enter(self):
    #     input_1 = self.get_element()
    #
    #     self.wait.until(EC.element_to_be_clickable(self.locator))
    #     self.action.send_keys_to_element(input_1, Keys.ENTER).perform()
