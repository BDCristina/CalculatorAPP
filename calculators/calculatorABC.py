""" in acest fisier implementam clasa abstracta calculator cu metoda abstrata calculate(),
aceasta metoda va avea implemnetare diferita in clasele ce mostenesc aceasta clasa abc """

from abc import ABC, abstractmethod


class CalculatorABC(ABC):

    def __init__(self, initial_value: 0.0):
        self._current_value = initial_value

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def display_result(self):
        pass

    @property
    def current_value(self):
        pass

    @current_value.setter
    def current_value(self, new_current_value):
        self._current_value = new_current_value

    @current_value.getter
    def current_value(self):
        return self._current_value
