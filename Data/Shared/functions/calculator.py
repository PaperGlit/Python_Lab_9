"""Calculates data after all the verifications"""
import global_variables
from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators

def calculate(num1, num2, operator):
    """Does the basic calculation of 2 numbers and an operator"""
    try:
        num1 = Validators.validate_number(num1, global_variables.DIGITS)
        num2 = Validators.validate_number(num2, global_variables.DIGITS)
    except ValueError as e:
        raise e
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        case "^":
            result = num1 ** num2
        case "root":
            result = num1 ** (1 / num2)
        case "%":
            result = num1 % num2
        case _:
            raise ValueError("Invalid operator")
    History.write(num1, num2, operator, result)
    return round(result, global_variables.DIGITS)
