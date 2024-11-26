"""A collection of different validators"""
import os
import global_variables
from Data.Shared.classes.history import History
from Data.Shared.classes.data_io import DataIO
from Data.Lab5.BLL.classes.cube import Cube
from Data.Lab5.BLL.classes.pyramid import Pyramid
from Data.Lab5.BLL.classes.sphere import Sphere
from Data.Shared.functions.logger import logger


class Validators:
    """A collection of different validators"""
    @staticmethod
    def validate_digits(digits_prompt):
        """Validates digits"""
        try:
            digits = int(digits_prompt)
            if digits >= 0:
                return digits
            logger.warning("Error: Invalid input")
            print("Invalid input, please enter a valid non-negative integer number")
        except ValueError:
            logger.warning("Error: Invalid input")
            print("Invalid input, please enter a valid non-negative integer number")
        return 3

    @staticmethod
    def validate_memory(operation, num):
        """Validates memory"""
        match operation:
            case "ms":
                global_variables.MEMORY = num
                print("Memory value stored! Current value: " + str(global_variables.MEMORY))
            case "m+":
                num_sum = global_variables.MEMORY + num
                History.write(str(global_variables.MEMORY), str(num), "+", str(num_sum))
                global_variables.MEMORY += num
                print("Memory value updated and saved into history! Current value: " +
                      str(global_variables.MEMORY))
            case "m-":
                num_diff = global_variables.MEMORY - num
                History.write(str(global_variables.MEMORY), str(num), "-", str(num_diff))
                global_variables.MEMORY -= num
                print("Memory value updated and saved into history! Current value: " +
                      str(global_variables.MEMORY))
            case _:
                logger.warning("Error occurred during memory validation")
                raise ValueError("Error occurred during memory validation")

    @staticmethod
    def validate_num(num_prompt="Enter the number (or MR / MC)"):
        """Validates the number or memory operation"""
        while True:
            value = (input(num_prompt)).lower()
            if value.lower() == "mr":
                recovered_value = round(global_variables.MEMORY, global_variables.DIGITS)
                print("Recovered value: " + str(recovered_value))
                return recovered_value
            if value.lower() == "mc":
                global_variables.memory = 0.0
                print("Memory cleared!")
            else:
                try:
                    return round(float(value), global_variables.DIGITS)
                except ValueError:
                    logger.warning("Error occurred during memory validation")
                    print("Please enter a valid number / memory operation")

    @staticmethod
    def validate_number(value, digits):
        """Validates number"""
        try:
            return round(float(value), digits)
        except ValueError:
            logger.warning("Error occurred during number validation")
            raise ValueError("Please enter a valid number")

    @staticmethod
    def validate_operator():
        """Validates operator"""
        while True:
            operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
            if (operator in global_variables.OPERANDS or operator
                    in global_variables.MEMORY_OPERATIONS):
                return operator
            logger.warning("Error occurred during operator validation")
            print("Please enter a valid operator")

    @staticmethod
    def validate_main_prompt(prompt, console):
        """Validates main prompt"""
        match prompt:
            case "1":
                logger.info("[Lab 4] Started entering text")
                console.enter_text()
                return True
            case "2":
                logger.info("[Lab 4] Started changing symbols")
                console.change_symbols()
                return True
            case "3":
                logger.info("[Lab 4] Started changing width and height")
                console.change_width_and_height()
                return True
            case "4":
                logger.info("[Lab 4] Started changing color")
                console.change_color()
                return True
            case "5":
                logger.info("[Lab 4] Started changing position")
                console.justify()
                return True
            case _:
                return False

    @staticmethod
    def save_file_prompt(prompt, text):
        """Validates text and saves it to a file"""
        if prompt == "y":
            try:
                DataIO.upload_to_file(text)
            except IOError:
                logger.warning("Error occurred during file upload")
                print("The file could not be uploaded, please try again")

    @staticmethod
    def validate_shading(prompt, console, shading_type):
        """Validates shading"""
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
            logger.warning("Error occurred during shading validation")
            print("Please enter a valid shading symbol (only one allowed)")

    @staticmethod
    def validate_dimensions(prompt, console):
        """Validates dimensions"""
        while True:
            try:
                width = int(prompt)
                console.ascii.WIDTH = width
                print("Width changed successfully")
                return
            except ValueError:
                logger.warning("Error occurred during dimensions validation")
                print("Please enter an integer")

    @staticmethod
    def validate_color(prompt, console):
        """Validates color"""
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
                logger.warning("Error occurred during color validation")
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")
        return

    @staticmethod
    def validate_justify(prompt, console):
        """Validates justify"""
        match prompt:
            case "1":
                console.ascii.justify = "left"
            case "2":
                console.ascii.justify = "center"
            case "3":
                console.ascii.justify = "right"
            case "_":
                logger.warning("Error occurred during justify validation")
                print("Invalid orientation choice, please try again.")
                return
        print("Orientation changed successfully")
        return

    @staticmethod
    def verify_width(width):
        """Validates width"""
        if width > 0:
            return width
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 200

    @staticmethod
    def validate_value(value, min_value, max_value):
        """Validates value"""
        try:
            result = int(value)
            if not min_value < result < max_value:
                raise ValueError("Incorrect value, please try again.")
        except ValueError:
            logger.warning("Error occurred during value validation")
            raise ValueError("Incorrect value, please try again.")

    @staticmethod
    def create_shape(shape, size):
        """Validates shape"""
        match shape:
            case "1":
                return Cube(size)
            case "2":
                return Pyramid(size)
            case "3":
                return Sphere(size)
            case _:
                logger.warning("Error occurred during shape validation")
                raise ValueError("Incorrect value, please try again.")

    @staticmethod
    def main_prompt(value, console):
        """Validates main prompt"""
        match value:
            case "1":
                logger.info("[Lab 5] Started creating shape")
                console.create_shape()
                return True
            case "2":
                logger.info("[Lab 5] Changing size")
                console.change_size()
                return True
            case "3":
                logger.info("[Lab 5] Moving shape")
                console.move_shape()
                return True
            case "4":
                logger.info("[Lab 5] Changing color")
                console.change_color()
                return True
            case "5":
                print(console.ascii)
                return True
            case "6":
                try:
                    DataIO.upload_to_file(console.ascii.__repr__())
                except IOError:
                    print("An error occurred during file upload, please check if "
                          "'Uploads' folder exists and try again")
            case _:
                return False
