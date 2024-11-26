"""Prints or verifies width of the ASCII art"""
import os
import math
import random
from pyfiglet import figlet_format, FigletFont
import global_variables


class Ascii:
    """The class for printing or verifying width of the ASCII art"""
    @staticmethod
    def verify_width(width):
        """Verifies the width of the ASCII art"""
        if width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        elif width > 0:
            return width
        else:
            return 220

    @staticmethod
    def print(text, is_random = False):
        """Prints the ASCII art to the console"""
        if is_random:
            font = random.choice(FigletFont.getFonts())
            color = "\033[" + str(random.randint(31, 39)) + "m"
        else:
            font = global_variables.FONT
            color = global_variables.COLOR
        art = figlet_format(text, font=font,
                            width=global_variables.WIDTH).strip_surrounding_newlines()
        art_height = len(art.splitlines())
        if global_variables.HEIGHT > art_height:
            height = global_variables.HEIGHT - art_height
        else:
            height = 0
        print(color + "\n" * math.ceil(height / 2) + art + "\n" * math.floor(height / 2) +
              global_variables.COLOR_RESET)
        return art
