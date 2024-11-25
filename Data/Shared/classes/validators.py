import os
import GlobalVariables as GlobalVariables
from Data.Shared.classes.history import History
from Data.Shared.classes.data_io import DataIO
from Data.Lab5.BLL.classes.cube import Cube
from Data.Lab5.BLL.classes.pyramid import Pyramid
from Data.Lab5.BLL.classes.sphere import Sphere


class Validators:
    @staticmethod
    def validate_digits(digits_prompt):
        try:
            digits = int(digits_prompt)
            if digits >= 0:
                return digits
            else:
                raise ValueError("Invalid input, please enter a valid non-negative integer number")
        except ValueError:
            raise ValueError("Invalid input, please enter a valid non-negative integer number")

    @staticmethod
    def validate_memory(operation, num):
        match operation:
            case "ms":
                GlobalVariables.memory = num
                print("Memory value stored! Current value: " + str(GlobalVariables.memory))
            case "m+":
                num_sum = GlobalVariables.memory + num
                History.write(str(GlobalVariables.memory), str(num), "+", str(num_sum))
                GlobalVariables.memory += num
                print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
            case "m-":
                num_diff = GlobalVariables.memory - num
                History.write(str(GlobalVariables.memory), str(num), "-", str(num_diff))
                GlobalVariables.memory -= num
                print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
            case _:
                raise ValueError("Error occurred during memory validation")

    @staticmethod
    def validate_num(num_prompt="Enter the number (or MR / MC)"):
        while True:
            value = (input(num_prompt)).lower()
            if value.lower() == "mr":
                recovered_value = round(GlobalVariables.memory)
                print("Recovered value: " + str(recovered_value))
                return round(GlobalVariables.memory, recovered_value)
            elif value.lower() == "mc":
                GlobalVariables.memory = 0.0
                print("Memory cleared!")
            else:
                try:
                    return round(float(value))
                except ValueError:
                    raise ValueError("Please enter a valid number / memory operation")

    @staticmethod
    def validate_number(value, digits):
        try:
            return round(float(value), digits)
        except ValueError:
            raise ValueError("Please enter a valid number")

    @staticmethod
    def validate_operator():
        while True:
            operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
            if operator in GlobalVariables.operands or operator in GlobalVariables.memory_operations:
                return operator
            else:
                raise ValueError("Please enter a valid operator")

    @staticmethod
    def validate_main_prompt(prompt, console):
        match prompt:
            case "1":
                console.enter_text()
                return True
            case "2":
                console.change_symbols()
                return True
            case "3":
                console.change_width_and_height()
                return True
            case "4":
                console.change_color()
                return True
            case "5":
                console.justify()
                return True
            case _:
                return False

    @staticmethod
    def save_file_prompt(prompt, text):
        if prompt == "y":
            try:
                DataIO.upload_to_file(text)
            except IOError:
                print("The file could not be uploaded, please try again")

    @staticmethod
    def validate_shading(prompt, console, shading_type):
        while True:
            if prompt.strip() != "" or len(prompt) == 1:
                match shading_type:
                    case 1:
                        console.ascii.shadow = prompt
                    case 2:
                        console.ascii.text_s = prompt
                    case 3:
                        console.ascii.highlight = prompt
                    case _:
                        raise ValueError("Wrong type detected")
                return
            else:
                print("Please enter a valid shading symbol (only one allowed)")

    @staticmethod
    def validate_dimensions(prompt, console):
        while True:
            try:
                width = int(prompt)
                console.ascii.width = width
                print("Width changed successfully")
                return
            except ValueError:
                print("Please enter an integer")

    @staticmethod
    def validate_color(prompt, console):
        match prompt:
            case "1":
                console.ascii.color = "\033[31m"
            case "2":
                console.ascii.color = "\033[32m"
            case "3":
                console.ascii.color = "\033[33m"
            case "4":
                console.ascii.color = "\033[34m"
            case "5":
                console.ascii.color = "\033[35m"
            case "6":
                console.ascii.color = "\033[36m"
            case "7":
                console.ascii.color = "\033[37m"
            case "8":
                console.ascii.color = "random"
            case "0":
                console.ascii.color = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")
        return

    @staticmethod
    def validate_justify(prompt, console):
        match prompt:
            case "1":
                console.ascii.justify = "left"
            case "2":
                console.ascii.justify = "center"
            case "3":
                console.ascii.justify = "right"
            case "_":
                print("Invalid orientation choice, please try again.")
                return
        print("Orientation changed successfully")
        return

    @staticmethod
    def verify_width(width):
        if width > 0:
            return width
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 200

    @staticmethod
    def validate_value(value, min_value, max_value):
        try:
            result = int(value)
            if not (min_value < result < max_value):
                raise ValueError("Incorrect value, please try again.")
        except ValueError:
            raise ValueError("Incorrect value, please try again.")
        return result

    @staticmethod
    def create_shape(shape, size):
        match shape:
            case 1:
                return Cube(size)
            case 2:
                return Pyramid(size)
            case 3:
                return Sphere(size)
            case _:
                raise ValueError("Incorrect value, please try again.")

    @staticmethod
    def main_prompt(value, console):
        match value:
            case "1":
                console.create_shape()
            case "2":
                console.change_size()
            case "3":
                console.move_shape()
            case "4":
                console.change_color()
            case "5":
                print(console.shape)
            case _:
                raise ValueError("Incorrect value, please try again.")