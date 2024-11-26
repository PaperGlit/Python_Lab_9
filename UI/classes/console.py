"""The user interface of the lab work"""
import Data.Lab1.UI.classes.console
import Data.Lab2.UI.classes.console
import Data.Lab3.UI.classes.console
import Data.Lab4.UI.classes.console
import Data.Lab5.UI.classes.console
import Data.Lab6.UI.classes.console
import Data.Lab7.UI.classes.console
import Data.Lab8.UI.classes.console
from Data.Shared.functions.logger import logger


class Console:
    """The console class of this lab work"""
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Console, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        logger.info("Started the program")
        self.main()

    @staticmethod
    def main():
        """The main menu of this lab work"""
        while True:
            prompt = input("Select lab work (1-8): ")
            match prompt:
                case '1':
                    logger.info("Started Lab 1")
                    Data.Lab1.UI.classes.console.Console()
                case '2':
                    logger.info("Started Lab 2")
                    Data.Lab2.UI.classes.console.Console()
                case '3':
                    logger.info("Started Lab 3")
                    Data.Lab3.UI.classes.console.Console()
                case '4':
                    logger.info("Started Lab 4")
                    Data.Lab4.UI.classes.console.Console()
                case '5':
                    logger.info("Started Lab 5")
                    Data.Lab5.UI.classes.console.Console()
                case '6':
                    logger.info("Started Lab 6")
                    Data.Lab6.UI.classes.console.Console()
                case '7':
                    logger.info("Started Lab 7")
                    Data.Lab7.UI.classes.console.Console()
                case '8':
                    logger.info("Started Lab 8")
                    Data.Lab8.UI.classes.console.Console()
                case _:
                    logger.info("Ended the program")
                    break
            logger.info("Ended Lab %s", prompt)
