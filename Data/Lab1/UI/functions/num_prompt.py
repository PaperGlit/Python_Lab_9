def prompt(value):
    match value:
        case 1:
            return "Enter first number (or MR / MC): "
        case 2:
            return "Enter second number (or MR / MC): "
        case _:
            return