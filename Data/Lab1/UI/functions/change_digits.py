from Data.Shared.classes.validators import Validators


def change():
    while True:
        digits_prompt = input("Enter the amount of digits: ")
        digits = Validators.validate_digits(digits_prompt)
        if digits:
            print("Settings changed successfully")
            break
        else:
            print("Invalid input, please enter a valid non-negative integer number")