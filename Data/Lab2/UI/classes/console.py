"""The user interface of the lab work"""
import global_variables
from Data.Shared.functions.calculator import calculate
from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators
from Data.Shared.functions.logger import logger


class Console:
    """The class of the user interface of the lab work"""
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Console, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.main()

    @staticmethod
    def main():
        """The main menu of the lab work"""
        while True:
            case = input("\n1 - Calculate a number \n"
                         "2 - View history \n"
                         "3 - Additional settings \n"
                         "Your choice: ")
            match case:
                case "1":
                    try:
                        if Console.calculator():
                            return
                    except ValueError as e:
                        print(e)
                case "2":
                    History.read()
                case "3":
                    Console.settings()
                case _:
                    return

    @staticmethod
    def calculator():
        """Does all the verifications before calculating a number"""
        logger.info("[Lab 2] Started performing calculation")
        num1 = Validators.validate_num("\nEnter first number (or MR / MC): ")

        operator = Validators.validate_operator()
        if operator in global_variables.MEMORY_OPERATIONS:
            Validators.validate_memory(operator, num1)
            return False

        num2 = Validators.validate_num("Enter second number (or MR / MC): ")

        if operator == "/" and num2 == 0:
            print("Error: cannot divide by zero")
            return False

        result = calculate(num1, num2, operator)

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

    @staticmethod
    def settings():
        """Allows to change digits after a decimal point in a number or to clear history"""
        settings_prompt = input("\n1 - Change the amount of digits after "
                                "a decimal point in a number \n"
                                "2 - Clear history\n"
                                "Your choice: ")
        match settings_prompt:
            case "1":
                while True:
                    digits_prompt = input("\nEnter the amount of digits (Current value: " + str(
                        global_variables.DIGITS) + "): ")
                    digits = Validators.validate_digits(digits_prompt)
                    if digits:
                        print("Settings changed successfully\n")
                        break
                    print("Invalid input, please enter a valid non-negative integer number")
            case "2":
                History.clear()
                print("History cleared successfully")

            case _:
                print("Invalid input")
