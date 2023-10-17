""" in acest fisier implementam clasa CalculatorScientific(),
cu ajutorul ei adaugam funcționalitati aplicatiei calculator
necesare pentru calcul stiintific"""

from calculators.calculatorABC import CalculatorABC
import math


class CalculatorScientific(CalculatorABC):

    def __init__(self, initial_value=0.0):
        super().__init__(initial_value)

    def calculate(self, number):
        print("Selectați operația:")
        print("1. Putere")
        print("2. Radical")
        print("3. Logaritm")
        print("4. Exponențial")

        choice = input("Introduceți numărul operației: ")

        if choice == '1':
            exponent = float(input("Introduceți exponentul: "))
            self.power(number, exponent)
            self.display_result()
        elif choice == '2':
            self.square(number)
            self.display_result()
        elif choice == '3':
            self.logarithm(number)
            self.display_result()
        elif choice == '4':
            self.exponential(number)
            self.display_result()
        else:
            print("Opțiune invalidă")

    def power(self, number, exponent):
        self._current_value = number ** exponent

    def square(self, number):
        self._current_value = math.sqrt(number)

    def logarithm(self, number):
        self._current_value = math.log(number)

    def exponential(self, number):
        self._current_value = math.exp(number)

    def display_result(self):
        print(f"The result is {self._current_value}")
