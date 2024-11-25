from Data.Shared.classes.history import History
from Data.Lab1.UI.functions import calculator_settings
from Data.Lab1.BLL.functions import perform_calculation


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
                        if perform_calculation.perform():
                            return
                    case "2":
                        History.read()
                    case "3":
                        calculator_settings.settings()
                    case _:
                        return
            except Exception as e:
                print(e)