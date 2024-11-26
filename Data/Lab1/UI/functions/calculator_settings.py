"""A settings menu"""
from Data.Lab1.UI.functions import change_digits
from Data.Shared.classes.history import History


def settings():
    """Allows to change digits after a decimal point in a number or to clear history"""
    settings_prompt = input("1 - Change the amount of digits after a decimal point in a number, "
                            "2 - Clear history: ")

    match settings_prompt:
        case "1":
            change_digits.change()

        case "2":
            History.clear()
            print("History cleared successfully")

        case _:
            print("Invalid input")
