import random
import string
from Data.Shared.classes.validators import Validators
from Data.Shared.classes.incorrect_character_exception import IncorrectCharacterException


class Ascii:
    def __init__(self, text, width = 0, height = 0, color = "\033[39m", shadow = "#", text_s = "#", highlight = "#", justify = "left"):
        self.text = text
        self.shadow = shadow
        self.text_s = text_s
        self.highlight = highlight
        self.height = height
        self.width = Validators.verify_width(width)
        self.color = "\033[" + str(random.randint(31, 39)) + "m" if color == "random" else color
        self.color_reset = "\033[0m"
        self.justify = justify
        self.font = self.__load_font()

    def print(self):
        art = self.__format_art()
        print(self.color + art + self.color_reset)
        return art

    def __wrap_art(self):
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
                raise IncorrectCharacterException("The character " + char + " is not a valid character.")
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
        wrapped_art = self.__wrap_art()
        art_lines = []
        for chunk in wrapped_art:
            unsorted_art_list = []
            for art_char in chunk:
                font_art = self.font[art_char.upper()]
                formatted_font_art = (font_art.replace('*', self.highlight)
                                      .replace('#', self.text_s).replace('&', self.shadow))
                split_font_art = formatted_font_art.splitlines()
                unsorted_art_list.append(split_font_art)
            art_list = []
            for row in zip(*unsorted_art_list):
                row_str = "".join(row)
                match self.justify:
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
            art_lines.append("\n".join(art_list))
        art = "\n\n".join(art_lines)
        art_height = len(art.splitlines())
        height_diff = self.height - art_height
        padding = "\n" * (height_diff // 2) if height_diff > 0 else ""
        return padding + art + padding

    @staticmethod
    def __load_font():
        keys = (list(string.ascii_uppercase) + list(string.digits) +
                ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
                 "+", "[", "]", ";", ":", "'", '"', ",", ".", "/", "<", ">", "?", " "])
        font = {}
        with open("Data/Lab4/Sources/font.txt", "r") as file:
            i = 0
            for line in file:
                if line.strip() == "$":
                    i+= 1
                elif i < len(keys):
                    key = keys[i]
                    font[key] = font.get(key, "") + line
        return font