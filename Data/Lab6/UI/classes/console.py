from Data.Lab6.BLL.classes.calculator import Calculator
from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators
from Data.Shared.classes.unit_test import UnitTest
from GlobalVariables import memory_operations
import unittest


class Console:
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Console, self).__call__(*args, **kwargs)
        else:
            self._instances[self].__init__(*args, **kwargs)
        return self._instances[self]

    def __init__(self, digits = 3):
        self.digits = digits
        self.prompt()

    def prompt(self):
        while True:
            case = input("\n1 - Calculate a number \n"
                         "2 - View history \n"
                         "3 - Additional settings \n"
                         "4 - Unit test \n"
                         "Your choice: ")
            match case:
                case "1":
                    self.calculator()
                case "2":
                    History.read()
                case "3":
                    self.settings()
                case "4":
                    self.run_unit_tests()
                case _:
                    return

    @staticmethod
    def run_unit_tests():
        print("Running unit tests...\n")
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest)
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def calculator(self):
        num1 = Validators.validate_num("\nEnter first number (or MR / MC): ")
        operator = Validators.validate_operator()
        if operator in memory_operations:
            Validators.validate_memory(operator, num1)
            return False
        num2 = Validators.validate_num("Enter second number (or MR / MC): ")
        try:
            result = Calculator(num1, num2, operator, self.digits)
        except ZeroDivisionError:
            print("Error: cannot divide by zero")
            return False
        print("Result : " + str(result.result))
        try_again = input("\nCalculation has finished successfully! \n"
                          "Current options: \n"
                          "Try again? (Y / N) \n"
                          "Store a value into memory? (MS / M+ / M-) \n"
                          "Your choice: ").lower()
        if try_again in memory_operations:
            Validators.validate_memory(try_again, result.result)
        elif try_again == "y":
            return False
        else:
            return True


    def settings(self):
        settings_prompt = input("\n1 - Change the amount of digits after a decimal point in a number \n"
                                "2 - Clear history\n"
                                "Your choice: ")
        match settings_prompt:
            case "1":
                while True:
                    digits_prompt = input("\nEnter the amount of digits (Current value: " + str(self.digits) + "): ")
                    try:
                        self.digits = Validators.validate_digits(digits_prompt)
                        print("Settings changed successfully\n")
                        break
                    except ValueError as e:
                        print(e)
            case "2":
                History.clear()
                print("History cleared successfully")
            case _:
                print("Invalid input")