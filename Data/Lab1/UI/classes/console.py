"""Outputs the lab's main menu"""
from Data.Shared.classes.history import History
from Data.Lab1.UI.functions import calculator_settings
from Data.Lab1.BLL.functions import perform_calculation
from Data.Shared.functions.logger import logger


class Console:
    """The class of the main menu of this lab work"""
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Console, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.main()

    @staticmethod
    def main():
        """The main menu of this lab work"""
        while True:
            case = input("1 - Calculate a number, 2 - View history, 3 - Additional settings: ")
            try:
                match case:
                    case "1":
                        logger.info("[Lab 1] Started performing calculation")
                        if perform_calculation.perform():
                            return
                    case "2":
                        logger.info("[Lab 2] Read history")
                        History.read()
                    case "3":
                        logger.info("[Lab 3] Opened setting menu")
                        calculator_settings.settings()
                    case _:
                        return
            except ValueError as e:
                print(e)
