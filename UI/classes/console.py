import Data.Lab1.UI.classes.console
import Data.Lab2.UI.classes.console
import Data.Lab3.UI.classes.console
import Data.Lab4.UI.classes.console
import Data.Lab5.UI.classes.console
import Data.Lab6.UI.classes.console
import Data.Lab7.UI.classes.console
import Data.Lab8.UI.classes.console


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
            prompt = input("Select lab work (1-8): ")
            match prompt:
                case '1':
                    Data.Lab1.UI.classes.console.Console()
                case '2':
                    Data.Lab2.UI.classes.console.Console()
                case '3':
                    Data.Lab3.UI.classes.console.Console()
                case '4':
                    Data.Lab4.UI.classes.console.Console()
                case '5':
                    Data.Lab5.UI.classes.console.Console()
                case '6':
                    Data.Lab6.UI.classes.console.Console()
                case '7':
                    Data.Lab7.UI.classes.console.Console()
                case '8':
                    Data.Lab8.UI.classes.console.Console()
                case _:
                    break