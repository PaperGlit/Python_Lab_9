import os


try:
    width = os.get_terminal_size().columns
except OSError:
    width = 220
height = 0
font = 'slant'
color = "\033[39m"
color_reset = "\033[0m"
memory_operations = ["ms", "m+", "m-"]
operands = ["+", "-", "*", "/", "^", "root", "%"]
memory = 0.0
digits = 3
base_api_url = "https://jsonplaceholder.typicode.com"
link_regex = r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,6}(\/[^\s]*)?$'
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_regex = r'^\+380(20|39|50|63|66|67|68|73|75|77|89|91|92|93|94|95|96|97|98|99)\d{7}$'
header_style = "bold white on blue"
entity_map = {
    "1": "posts",
    "2": "comments",
    "3": "albums",
    "4": "photos",
    "5": "todos",
    "6": "users"}