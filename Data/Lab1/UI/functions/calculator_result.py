"""Checks if division by zero is performed"""
import global_variables
from Data.Shared.functions.calculator import calculate
from Data.Shared.functions.logger import logger


def find(num1, num2, operator):
    """If there is a division by zero, halts the operation, else continues calculating"""
    if operator == "/" and num2 == 0:
        print("Error: cannot divide by zero")
        logger.warning("[Lab 1] Error: cannot divide by zero")
        return False
    result = calculate(num1, num2, operator)
    result = round(result, global_variables.DIGITS)
    print("Result : " + str(result))
    return result
