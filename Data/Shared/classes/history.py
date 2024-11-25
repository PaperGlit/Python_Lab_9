import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class History:
    @staticmethod
    def clear():
        logger.info("Clearing history")
        with open("Exports/history.txt", "w"):
            pass

    @staticmethod
    def read():
        logger.info("Reading history...")
        with open("Exports/history.txt", "r") as file:
            history = file.read()
            if not history:
                print("Your history is empty!")
            else:
                print("Your history:\n" + history)

    @staticmethod
    def write(num1, num2, operator, result):
        logger.info("Writing history...")
        with open("Exports/history.txt", "a") as history_file:
            history_file.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")