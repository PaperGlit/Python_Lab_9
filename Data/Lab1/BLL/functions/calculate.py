def calculate(num1, num2, operator):
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