from Data.Shared.classes.history import History
from Data.Shared.classes.validators import Validators


class Calculator:
    digits = 3

    def __init__(self, num1, num2, operator, digits=0):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = round(self.calculate(), digits)
        self.digits = digits
        History.write(self.num1, self.num2, self.operator, self.result)

    def calculate(self):
        try:
            self.num1 = Validators.validate_number(self.num1, self.digits)
            self.num2 = Validators.validate_number(self.num2, self.digits)
        except ValueError as e:
            raise e
        match self.operator:
            case "+":
                return self.num1 + self.num2
            case "-":
                return self.num1 - self.num2
            case "*":
                return self.num1 * self.num2
            case "/":
                if self.num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return self.num1 / self.num2
            case "^":
                return self.num1 ** self.num2
            case "root":
                return self.num1 ** (1 / self.num2)
            case "%":
                return self.num1 % self.num2
            case _:
                raise ValueError("Invalid operator")