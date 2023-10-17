"""in cadrul acestui fisier vom face teste pentru functionalitatile Calculatorului unui programator
"""

import unittest
from calculators.programmer_calculator import CalculatorProgrammer


class TestCalculatorProgrammer(unittest.TestCase):

    def test_binary_conversion(self):
        calc = CalculatorProgrammer("10")
        calc.calculate("bin", None)
        self.assertEqual(calc._current_value, "0b1010")

    def test_octal_conversion(self):
        calc = CalculatorProgrammer("10")
        calc.calculate("oct", None)
        self.assertEqual(calc._current_value, "0o12")

    def test_hexadecimal_conversion(self):
        calc = CalculatorProgrammer("10")
        calc.calculate("hex", None)
        self.assertEqual(calc._current_value, "0x10")

    def test_binary_to_decimal_conversion(self):
        calc = CalculatorProgrammer(10.0)
        calc.calculate("bin-dec", '0b1010')
        self.assertEqual(calc._current_value, 10.0)

    def test_decimal_to_binary_conversion(self):
        calc = CalculatorProgrammer(10.0)
        calc.calculate("dec-bin", 10)
        self.assertEqual(calc._current_value, '0b1010')


if __name__ == '__main__':
    unittest.main()


"""
Pentru a rula teste, poți folosi comanda python -m unittest tests.test_programmer_calculator 
pentru a rula testele dintr-un fișier specific sau python -m unittest 
discover tests pentru a rula toate testele din directorul tests.
"""