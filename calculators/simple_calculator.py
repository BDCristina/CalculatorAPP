""" in acest fisier implementam clasa calculator(),
cu ajutorul ei putem face oferatiile de baza a aplicatiei calculator """

from calculators.calculatorABC import CalculatorABC


class CalculatorSimple(CalculatorABC):

    def __init__(self, initial_value= 0.0):
        super().__init__(initial_value)

    def calculate(self, operation, number):
        if operation == '+':
            self.add(number)
        elif operation == '-':
            self.subtract(number)
        elif operation == '*':
            self.multiply(number)
        elif operation == '/':
            self.divide(number)
        else:
            print("Invalid operation")

    def display_result(self):
        print(f"The result is {self._current_value}")

    def add(self, number):
        self._current_value += number

    def subtract(self, number):
        self._current_value -= number

    def multiply(self, number):
        self._current_value *= number

    def divide(self, number):
        if number != 0:
            self._current_value /= number
        else:
            print("Division by zero")


