import Data.Lab1.UI.classes.console
import Data.Lab2.UI.classes.console
import Data.Lab3.UI.classes.console
import Data.Lab4.UI.classes.console
import Data.Lab5.UI.classes.console
import Data.Lab6.UI.classes.console
import Data.Lab7.UI.classes.console
import Data.Lab8.UI.classes.console
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
        logger.info("Started the program")
        self.main()

    def main(self):
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
            logger.info(f"Ended Lab {prompt}")