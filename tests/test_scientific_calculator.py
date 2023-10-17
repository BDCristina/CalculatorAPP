"""
in cadrul acestui fisier vom face teste pentru functionalitatile Calculatorului de scientific
"""
import unittest
from calculators.scientific_calculator import CalculatorScientific


class TestScientificCalculator(unittest.TestCase):

    def test_power(self):
        calc = CalculatorScientific(7)
        calc.calculate(7) # adauga 2 cand cere valoarea exponentului
        self.assertEqual(calc._current_value, 49)

    def test_square(self):
        calc = CalculatorScientific(25)
        calc.calculate(25) # 25
        self.assertEqual(calc._current_value, 5.0)

    def test_logarithm(self):
        calc = CalculatorScientific(100)
        #calc.calculate() # 10
        calc.logarithm(10)
        self.assertEqual(calc._current_value, 2.302585092994046)

    def test_exponential(self):
        calc = CalculatorScientific(2)
        #calc.calculate() # 3
        calc.exponential(3)
        self.assertEqual(calc._current_value, 20.085536923187668)



if __name__ == '__main__':
    unittest.main()



"""
Pentru a rula teste, poți folosi comanda python -m unittest tests.test_scientific_calculator 
pentru a rula testele dintr-un fișier specific sau python -m unittest 
discover tests pentru a rula toate testele din directorul tests.
"""
