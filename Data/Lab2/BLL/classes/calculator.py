from Data.Shared.classes.history import History


class Calculator:
    def __init__(self, num1, num2, operator, digits=3):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = round(Calculator.calculate(num1, num2, operator), digits)
        self.digits = digits
        History.write(self.num1, self.num2, self.operator, self.result)

    @staticmethod
    def calculate(num1 : float, num2 : float, operator : str):
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return num1 / num2
            case "^":
                return num1 ** num2
            case "root":
                return num1 ** (1 / num2)
            case "%":
                return num1 % num2
            case _:
                return 0.0