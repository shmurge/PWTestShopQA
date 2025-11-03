import allure

from elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, page, name, selector):
        super().__init__(page, name, selector)

        self.name = f'Кнопка: {name}'
