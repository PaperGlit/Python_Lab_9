"""The module that does the ASCII art for this lab work"""
import random
import string
import global_variables
from Data.Shared.classes.validators import Validators
from Data.Shared.classes.incorrect_character_exception import IncorrectCharacterException


class Ascii:
    """The class of the ASCII art"""
    def __init__(self, text, color):
        self.text = text
        self.width = Validators.verify_width(global_variables.WIDTH)
        self.color = "\033[" + str(random.randint(31, 39)) + "m" \
            if color == "random" else color
        self.font = self.load_font()

    def print(self):
        """Print the ASCII art"""
        art = self.__format_art()
        print(self.color + art + global_variables.COLOR_RESET)
        return art

    def __wrap_art(self):
        """Performs the text wrapping for the ASCII art
        if the set width is below the art's width"""
        wrapped_text = []
        length = 0
        current_line = ""
        for char in self.text.upper():
            if char in ["@", "#"]:
                length += 9
            if char in ["M", "W", "4", "*"]:
                length += 8
            elif char in self.font:
                length += 7
            else:
                raise IncorrectCharacterException("The character " + char +
                                                  " is not a valid character.")
            if length > self.width:
                wrapped_text.append(current_line)
                current_line = char
                length = 8 if char in ["M", "W", "4"] else 7
            else:
                current_line += char
        if current_line:
            wrapped_text.append(current_line)
        return wrapped_text

    def __format_art(self):
        """Formats the ASCII art"""
        wrapped_art = self.__wrap_art()
        art_lines = []
        for chunk in wrapped_art:
            unsorted_art_list = []
            for art_char in chunk:
                font_art = self.font[art_char.upper()]
                formatted_font_art = (font_art.replace('*', global_variables.HIGHLIGHT)
                                      .replace('#', global_variables.TEXT_SYMBOL).
                                      replace('&', global_variables.SHADOW))
                split_font_art = formatted_font_art.splitlines()
                unsorted_art_list.append(split_font_art)
            art_list = self.__justify_font(unsorted_art_list)
            art_lines.append("\n".join(art_list))
        art = "\n\n".join(art_lines)
        art_height = len(art.splitlines())
        height_diff = global_variables.HEIGHT - art_height
        padding = "\n" * (height_diff // 2) if height_diff > 0 else ""
        return padding + art + padding

    def __justify_font(self, unsorted_art_list):
        """Justifies the ASCII art"""
        art_list = []
        for row in zip(*unsorted_art_list):
            row_str = "".join(row)
            match global_variables.JUSTIFY:
                case "left":
                    art_list.append(row_str)
                case "center":
                    width = self.width - len(row_str)
                    padding = " " * (width // 2)
                    art_list.append(padding + row_str + padding)
                case "right":
                    width = self.width - len(row_str)
                    padding = " " * width
                    art_list.append(padding + row_str)
        return art_list

    @staticmethod
    def load_font():
        """Loads the ASCII art font from the file"""
        keys = (list(string.ascii_uppercase) + list(string.digits) +
                ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
                 "+", "[", "]", ";", ":", "'", '"', ",", ".", "/", "<", ">", "?", " "])
        font = {}
        with open("Data/Lab4/Sources/font.txt", "r", encoding="utf-8") as file:
            i = 0
            for line in file:
                if line.strip() == "$":
                    i+= 1
                elif i < len(keys):
                    key = keys[i]
                    font[key] = font.get(key, "") + line
        return font
