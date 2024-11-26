"""All the semi-constant values are stored here."""
import os


try:
    WIDTH = os.get_terminal_size().columns
except OSError:
    WIDTH = 220
HEIGHT = 0
FONT = 'slant'
COLOR = "\033[39m"
COLOR_RESET = "\033[0m"
JUSTIFY = "left"
SHADOW = "#"
TEXT_SYMBOL = "#"
HIGHLIGHT = "#"
MEMORY_OPERATIONS = ["ms", "m+", "m-"]
OPERANDS = ["+", "-", "*", "/", "^", "root", "%"]
MEMORY = 0.0
DIGITS = 3
BASE_API_URL = "https://jsonplaceholder.typicode.com"
LINK_REGEX = r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,6}(\/[^\s]*)?$'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+380(20|39|50|63|66|67|68|73|75|77|89|91|92|93|94|95|96|97|98|99)\d{7}$'
HEADER_STYLE = "bold white on blue"
ENTITY_MAP = {
    "1": "posts",
    "2": "comments",
    "3": "albums",
    "4": "photos",
    "5": "todos",
    "6": "users"}
