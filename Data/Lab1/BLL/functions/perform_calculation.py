"""Compiles all the validators and calculates a number"""
from global_variables import MEMORY_OPERATIONS
from Data.Lab1.UI.functions import try_again, num_prompt, calculator_result
from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators


def perform():
    """Gets 2 numbers from a user input and validates them before sending them for calculation"""
    num1 = Validators.validate_num(num_prompt.prompt(1))

    operator = Validators.validate_operator()
    if operator in MEMORY_OPERATIONS:
        Validators.validate_memory(operator, num1)
        return False

    num2 = Validators.validate_num(num_prompt.prompt(2))

    result = calculator_result.find(num1, num2, operator)

    if not result:
        return False

    History.write(num1, num2, operator, result)
    print("The operation was saved into history")

    return try_again.parse(result)
