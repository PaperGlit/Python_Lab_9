from Data.Shared.classes.history import History
from Data.Lab1.UI.functions import calculator_settings
from Data.Lab1.BLL.functions import perform_calculation
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class Console:
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Console, self).__call__(*args, **kwargs)
        else:
            self._instances[self].__init__(*args, **kwargs)
        return self._instances[self]

    def __init__(self):
        self.main()

    @staticmethod
    def main():
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
            except Exception as e:
                print(e)