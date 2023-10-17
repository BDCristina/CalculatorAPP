""" in acest fisier implementam clasa CalculatorProgrammer(),
cu ajutorul ei adaugam funcționalitati aplicatiei calculator
necesare pentru un programator"""

from calculators.calculatorABC import CalculatorABC


class CalculatorProgrammer(CalculatorABC):

    def __init__(self, initial_value: str):
        super().__init__(initial_value)


    def calculate(self, operation, number):
        if operation == "bin":
            self.binary()
        elif operation == "oct":
            self.octal()
        elif operation == "hex":
            self.hexadecimal()
        elif operation == "dec-bin":
            self.decimal_to_binary(number)
        elif operation == "bin-dec":
            self.binary_to_decimal(number)
        else:
            print("Invalid operation")

    def display_result(self):
        print(f"The result is {self._current_value}")

    def binary(self):
        try:
            # Verificați dacă valoarea are prefixul '0x' pentru hexazecimal
            if self._current_value.startswith("0x"):
                # Eliminați prefixul '0x' pentru conversia corectă
                hex_value = self._current_value[2:]
                # Convertiți valoarea într-un număr întreg în baza 16 (hexazecimal)
                int_value = int(hex_value, 16)  # De exemplu, '10' pentru '0x10'
            else:
                # Convertiți valoarea într-un număr întreg în baza 10 (zecimal)
                int_value = int(self._current_value, 10)

            # Convertiți numărul întreg în format binar
            binary_number = bin(int_value)
            self._current_value = binary_number
            print("Binary:", binary_number)
        except ValueError:
            print("Invalid value for binary conversion:", self._current_value)

    def octal(self):
        try:
            # Verificați dacă valoarea are prefixul '0x' pentru hexazecimal
            if self._current_value.startswith("0x"):
                # Eliminați prefixul '0x' pentru conversia corectă
                hex_value = self._current_value[2:]
                # Convertiți valoarea într-un număr întreg în baza 16 (hexazecimal)
                int_value = int(hex_value, 16)
                # Convertiți numărul întreg în format octal
                octal_number = oct(int_value)
                self._current_value = octal_number
                print("Octal:", octal_number)
            else:
                # Convertiți valoarea într-un număr întreg în baza 10 (zecimal)
                int_value = int(self._current_value, 10)
                # Convertiți numărul întreg în format octal
                octal_number = oct(int_value)
                self._current_value = octal_number
                print("Octal:", octal_number)
        except ValueError:
            print("Invalid value for octal conversion:", self._current_value)

    def hexadecimal(self):

        try:
            # convertim valoarea într-un număr întreg
            int_value = int(self._current_value, 16)  # Presupunând că valoarea este în format binar (0b1010)
            hex_number = hex(int_value)
            self._current_value = hex_number
            print("Hexadecimal:", hex_number)
        except ValueError:
            print("Invalid hexadecimal value:", self._current_value)


    def decimal_to_binary(self, decimal_number):
        if decimal_number is not None:
            binary_number = bin(int(decimal_number))
            self._current_value = binary_number
            print(f'Decimal {decimal_number} to Binay: ', binary_number)
        else:
            print("Invalid operation: Decimal to Binary")

    def binary_to_decimal(self, binary_number):
        if binary_number is not None:
            decimal_number = int(binary_number, 2)
            self._current_value = decimal_number
            print(f'Binary {binary_number} to Decimal: ', decimal_number)
        else:
            print("Invalid operation: Binary to Decimal")
