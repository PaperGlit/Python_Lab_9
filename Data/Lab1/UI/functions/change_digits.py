from Data.Shared.classes.validators import Validators
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

def change():
    while True:
        digits_prompt = input("Enter the amount of digits: ")
        digits = Validators.validate_digits(digits_prompt)
        if digits:
            print("Settings changed successfully")
            break
        else:
            logger.warning("[Lab 1] Error occurred during 'change digits' process")
            print("Invalid input, please enter a valid non-negative integer number")