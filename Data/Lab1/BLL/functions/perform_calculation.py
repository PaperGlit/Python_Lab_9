from Data.Lab1.UI.functions import try_again, num_prompt, calculator_result
from Data.Shared.classes.history import History
from GlobalVariables import memory_operations
from Data.Shared.classes.validators import Validators


#False - continue; True - break
def perform():
    num1 = Validators.validate_num(num_prompt.prompt(1))

    operator = Validators.validate_operator()
    if operator in memory_operations:
        Validators.validate_memory(operator, num1)
        return False

    num2 = Validators.validate_num(num_prompt.prompt(2))

    result = calculator_result.find(num1, num2, operator)

    if not result:
        return False

    History.write(num1, num2, operator, result)
    print("The operation was saved into history")

    return try_again.parse(result)