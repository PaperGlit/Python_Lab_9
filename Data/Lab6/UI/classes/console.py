"""The user interface of the lab work"""
import unittest
import global_variables
from Data.Shared.functions.calculator import calculate
from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators
from Data.Shared.classes.unit_test import UnitTest
from Data.Shared.functions.logger import logger
from Data.Shared.classes.unit_test import UnitTest

class Console:
    """The console class of this lab work"""
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Console, cls).__new__(cls)
        return cls.instance

    def __init__(self, digits = 3):
        self.digits = digits
        self.main()

    def main(self):
        """The main menu of this lab work"""
        while True:
            case = input("\n1 - Calculate a number \n"
                         "2 - View history \n"
                         "3 - Additional settings \n"
                         "4 - Unit test \n"
                         "Your choice: ")
            match case:
                case "1":
                    logger.info("[Lab 6] Started performing calculation")
                    try:
                        self.calculator()
                    except ValueError as e:
                        print(e)
                case "2":
                    logger.info("[Lab 6] Read history")
                    History.read()
                case "3":
                    logger.info("[Lab 6] Opened setting menu")
                    self.settings()
                case "4":
                    logger.info("[Lab 6] Started unit tests")
                    UnitTest.run_unit_tests()
                case _:
                    return

    @staticmethod
    def calculator():
        """Does all the verifications before calculating a number"""
        num1 = Validators.validate_num("\nEnter first number (or MR / MC): ")
        operator = Validators.validate_operator()
        if operator in global_variables.MEMORY_OPERATIONS:
            Validators.validate_memory(operator, num1)
            return False
        num2 = Validators.validate_num("Enter second number (or MR / MC): ")
        try:
            result = calculate(num1, num2, operator)
        except ZeroDivisionError:
            print("Error: cannot divide by zero")
            return False
        print("Result : " + str(result))
        try_again = input("\nCalculation has finished successfully! \n"
                          "Current options: \n"
                          "Try again? (Y / N) \n"
                          "Store a value into memory? (MS / M+ / M-) \n"
                          "Your choice: ").lower()
        if try_again in global_variables.MEMORY_OPERATIONS:
            Validators.validate_memory(try_again, result)
            return True
        if try_again == "y":
            return False
        return True

    def settings(self):
        """Allows to change digits after a decimal point in a number or to clear history"""
        settings_prompt = input("\n1 - Change the amount of digits"
                                " after a decimal point in a number \n"
                                "2 - Clear history\n"
                                "Your choice: ")
        match settings_prompt:
            case "1":
                while True:
                    digits_prompt = input("\nEnter the amount of digits (Current value: "
                                          + str(self.digits) + "): ")
                    try:
                        self.digits = Validators.validate_digits(digits_prompt)
                        global_variables.DIGITS = self.digits
                        print("Settings changed successfully\n")
                        break
                    except ValueError as e:
                        print(e)
            case "2":
                History.clear()
                print("History cleared successfully")
            case _:
                print("Invalid input")
