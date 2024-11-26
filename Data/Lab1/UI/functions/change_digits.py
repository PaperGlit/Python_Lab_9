"""Changes the amount of digits in a number after a decimal point"""
from Data.Shared.classes.validators import Validators
from Data.Shared.functions.logger import logger


def change():
    """Verifies if the value input by the user is viable, then changes the value"""
    while True:
        digits_prompt = input("Enter the amount of digits: ")
        digits = Validators.validate_digits(digits_prompt)
        if digits:
            print("Settings changed successfully")
            break
        logger.warning("[Lab 1] Error occurred during 'change digits' process")
        print("Invalid input, please enter a valid non-negative integer number")
