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

    def fill_autocomplete_input(self, data, element=None):
        element = element if element else self.find_element()
        element.fill(data)
        element.press('Enter')

        return data

    def get_input_value(self, element=None):
        element = element if element else self.find_element()

        return element.input_value()
