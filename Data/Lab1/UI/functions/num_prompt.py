"""Used to output the correct string for the number input"""
def prompt(value):
    """Also includes memory operations"""
    match value:
        case 1:
            return "Enter first number (or MR / MC): "
        case 2:
            return "Enter second number (or MR / MC): "
        case _:
            return ""
