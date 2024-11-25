import GlobalVariables as Globals
from Data.Lab1.BLL.functions import calculate
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

def find(num1, num2, operator):
    if operator == "/" and num2 == 0:
        print("Error: cannot divide by zero")
        logger.warning("[Lab 1] Error: cannot divide by zero")
        return False
    else:
        result = calculate.calculate(num1, num2, operator)
        result = round(result, Globals.digits)
        print("Result : " + str(result))
        return result