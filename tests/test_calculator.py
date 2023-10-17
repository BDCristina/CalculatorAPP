"""in cadrul acestui fisier vom face teste pentru functionalitatile Calculatorului de baza
"""

import unittest
from calculators.simple_calculator import CalculatorSimple

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = CalculatorSimple(5)
        calc.calculate("+", 5)
        self.assertEqual(calc._current_value, 10)

    def test_subtract(self):
        calc = CalculatorSimple(10)
        calc.calculate("-", 5)
        self.assertEqual(calc._current_value, 5.0)

    def test_multiply(self):
        calc = CalculatorSimple(10)
        calc.calculate("*", 5)
        self.assertEqual(calc._current_value, 50)

    def test_divide(self):
        calc = CalculatorSimple(10)
        calc.calculate("/", 5)
        self.assertEqual(calc._current_value, 2.0)

if __name__ == '__main__':
    unittest.main()


"""
Pentru a rula teste, poți folosi comanda python -m unittest tests.test_calculator 
pentru a rula testele dintr-un fișier specific sau python -m unittest 
discover tests pentru a rula toate testele din directorul tests.
"""
