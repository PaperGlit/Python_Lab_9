"""Manages the history functionality"""
from Data.Shared.functions.logger import logger


class History:
    """The class that manages the history functionality"""
    @staticmethod
    def clear():
        """Clears the history"""
        logger.info("Clearing history")
        with open("Exports/history.txt", "w", encoding="utf-8"):
            pass

    @staticmethod
    def read():
        """Reads the history"""
        logger.info("Reading history...")
        with open("Exports/history.txt", "r", encoding="utf-8") as file:
            history = file.read()
            if not history:
                print("Your history is empty!")
            else:
                print("Your history:\n" + history)

    @staticmethod
    def write(num1, num2, operator, result):
        """Writes the operation into the history"""
        logger.info("Writing history...")
        with open("Exports/history.txt", "a", encoding="utf-8") as history_file:
            history_file.write(str(num1) + " " + operator + " " +
                               str(num2) + " = " + str(result) + "\n")
