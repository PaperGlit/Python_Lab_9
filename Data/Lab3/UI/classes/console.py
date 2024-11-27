"""The console module of this lab work"""
import random
import textwrap
from pyfiglet import FigletFont, figlet_format
import global_variables
from Data.Lab3.BLL.classes.ascii import Ascii
from Data.Shared.classes.data_io import DataIO
from Data.Shared.classes.singleton import Singleton
from Data.Shared.functions.logger import logger


class Console(Singleton):
    """The console class of this lab work"""
    def __init__(self):
        self.main()

    @staticmethod
    def main():
        """The main menu of this lab work"""
        Ascii.print("ASCIIFY", True)
        while True:
            prompt = input("1 - Enter text\n"
                           "2 - Select font automatically\n"
                           "3 - Change font\n"
                           "4 - Current font\n"
                           "5 - Change width and height\n"
                           "6 - Change color\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    logger.info("[Lab 3] Started entering text")
                    Console.enter_text()
                case "2":
                    logger.info("[Lab 3] Selected font automatically")
                    Console.auto_font()
                case "3":
                    logger.info("[Lab 3] Changed font")
                    Console.change_font()
                case "4":
                    print("Current font: " + global_variables.FONT)
                case "5":
                    logger.info("[Lab 3] Changed width and height")
                    Console.change_width_and_height()
                case "6":
                    logger.info("[Lab 3] Changed color")
                    Console.change_color()
                case _:
                    return

    @staticmethod
    def enter_text():
        """Sends the text input by the user to printing, then allows them to save the art"""
        text = input("Enter text: ")
        ftext = Ascii.print(text)
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        if save_prompt == "y":
            try:
                DataIO.upload_to_file(ftext)
            except IOError:
                print("An error occurred during file upload, please check if 'Uploads' "
                      "folder exists and try again")

    @staticmethod
    def auto_font():
        """Automatically selects the font by the input characters"""
        text = input("Enter text: ")
        symbols = input("Enter a set of characters that should be in the ASCII art: ")
        font_symbols = set(symbols) | {" ", "\n"}
        fonts = FigletFont.getFonts()
        random.shuffle(fonts)
        for font in fonts:
            random_art = figlet_format(text, font=font, width=global_variables.WIDTH)
            random_art_chars = set(random_art)
            if all(char in [" ", "\n"] for char in random_art_chars):
                continue
            if all(char in font_symbols for char in random_art_chars):
                print("Found font:" + font)
                global_variables.FONT = font
                ftext = Ascii.print(text)
                save_prompt = input("Do you want to save the text? (y/n): ").lower()
                if save_prompt == "y":
                    try:
                        DataIO.upload_to_file(ftext)
                    except IOError:
                        print("An error occurred during file upload, please check if 'Uploads' "
                              "folder exists and try again")
                return
        print("No fonts were found, please try again with a wider set of characters")

    @staticmethod
    def change_font():
        """Changes the font of the art"""
        new_font = input("Enter the new font you want to choose\n"
                         "You can also use 'font' to see all fonts available or 'random' "
                         "to choose a random font\n"
                         "Your choice: ")
        if new_font in FigletFont.getFonts():
            global_variables.FONT = new_font
            print("Font changed successfully")
        elif new_font.lower() == "font":
            print("Available fonts:\n" + textwrap.fill(", ".join(FigletFont.getFonts()),
                                                       width=global_variables.WIDTH))
        elif new_font.lower() == "random":
            global_variables.FONT = random.choice(FigletFont.getFonts())
            print("Randomly selected font: " + global_variables.FONT)
        else:
            print("Invalid font")

    @staticmethod
    def change_width_and_height():
        """Changes the width and height of the art"""
        while True:
            width_prompt = input("Enter the width of an ASCII art\n"
                      "(any non-positive value will reset it to default values\n"
                      "Your choice: ")
            try:
                width = int(width_prompt)
                global_variables.WIDTH = Ascii.verify_width(width)
                print("Width changed successfully")
            except ValueError:
                print("Please enter an integer")
                continue
            height_prompt = input("Enter the height of an ASCII art\n"
                                  "(any non-positive value will reset it to default values\n"
                                  "Your choice: ")
            try:
                height = int(height_prompt)
                global_variables.HEIGHT = height
                print("Height changed successfully")
                break
            except ValueError:
                print("Please enter an integer")
                continue

    @staticmethod
    def change_color():
        """Changes the color of the art"""
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "0 - Default\n"
                             "Your choice: ")
        match color_prompt:
            case "1":
                global_variables.COLOR = "\033[31m"
            case "2":
                global_variables.COLOR = "\033[32m"
            case "3":
                global_variables.COLOR = "\033[33m"
            case "4":
                global_variables.COLOR = "\033[34m"
            case "5":
                global_variables.COLOR = "\033[35m"
            case "6":
                global_variables.COLOR = "\033[36m"
            case "7":
                global_variables.COLOR = "\033[37m"
            case "0":
                global_variables.COLOR = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")
