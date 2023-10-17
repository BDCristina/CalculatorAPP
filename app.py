"""in cadrul acestui fisier vom rula aplicatia CalculatorAPP cu ajutorul functei main()"""


from calculators.simple_calculator import CalculatorSimple
from calculators.scientific_calculator import CalculatorScientific
from calculators.programmer_calculator import CalculatorProgrammer

result = None


def main():
    while True:
        print('-------------------------')
        print("Select a calculator: ")
        print("1. Simple Calculator")
        print("2. Scientific Calculator")
        print("3. Programmer Calculator")
        print("4. Exit")
        print('--------------------------')

        choice = input("Enter your choise: 1 or 2 or 3: \n")
        print('--------------------------\n')

        global result

        if choice == "1":
            if result is None:
                result = float(input("Enter initial value: "))
            simple_calculator = CalculatorSimple(result)
            operation = input("Enter operation ( + , - , * , / ): \n ")
            number = float(input("Enter number: \n"))
            while result is not None:
                if operation == "+":
                    result = simple_calculator.calculate(operation, number)
                    simple_calculator.display_result()
                elif operation == "-":
                    result = simple_calculator.calculate(operation, number)
                    simple_calculator.display_result()
                elif operation == "*":
                    result = simple_calculator.calculate(operation, number)
                    simple_calculator.display_result()
                elif operation == "/":
                    if result != 0:
                        result = simple_calculator.calculate(operation, number)
                        simple_calculator.display_result()
                    else:
                        print("Division by zero.")
            result = simple_calculator._current_value

        elif choice == '2':
            if result is None:
                result = float(input("Enter initial value: "))
            scientific_calculator = CalculatorScientific(result)
            scientific_calculator.calculate(result)
            result = scientific_calculator._current_value

        elif choice == "3":
            if result is None:
                initial_value = input("Enter initial value (e.g., '10'): ")
                programmer_calculator = CalculatorProgrammer(initial_value)
            else:
                programmer_calculator = CalculatorProgrammer(str(result))

            operation = input("Enter operation (bin/oct/hex/dec-bin/bin-dec): ")
            number = input("Enter number (if required): ")

            programmer_calculator.calculate(operation, number)
            programmer_calculator.display_result()
            result = programmer_calculator.current_value
        elif choice == '4':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()
