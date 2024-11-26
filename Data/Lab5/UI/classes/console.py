"""The console module of this lab work"""
from Data.Shared.classes.validators import Validators


class Console:
    """The console class of this lab work"""
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Console, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.main()
        self.ascii = None

    def main(self):
        """The main menu of this lab work"""
        self.create_shape()
        while True:
            prompt = input("1 - Create a new shape\n"
                           "2 - Change shape's size\n"
                           "3 - Move shape\n"
                           "4 - Change shape's color\n"
                           "5 - Print shape\n"
                           "6 - Export shape\n"
                           "Your choice: ")
            if not Validators.main_prompt(prompt, self):
                return

    def create_shape(self):
        """The UI for the shape creation"""
        while True:
            shape_prompt = input("Select shape:\n"
                           "1 - Cube\n"
                           "2 - Pyramid\n"
                           "3 - Sphere\n"
                           "Your choice: ")
            try:
                 Validators.validate_value(shape_prompt, 0, 4)
            except ValueError as e:
                print(e)
                continue
            size_prompt = input("Enter shape's size (5-100): ")
            try:
                 Validators.validate_value(size_prompt, 4, 101)
                 size = int(size_prompt)
            except ValueError as e:
                print(e)
                continue
            self.ascii = Validators.create_shape(shape_prompt, size)
            print("Shape was created successfully")
            return

    def change_size(self):
        """The UI for the shape's size changing"""
        prompt = input("Change shape's new size (5-100): ")
        try:
            Validators.validate_value(prompt, 4, 101)
            size = int(prompt)
        except ValueError as e:
            print(e)
            return
        self.ascii.change_size(size)
        print("Shape's size was changed successfully")

    def move_shape(self):
        """The UI for moving the shape"""
        prompt_x = input("Move shape by (x) (-10-10): ")
        try:
            Validators.validate_value(prompt_x, -10, 10)
            x = int(prompt_x)
        except ValueError as e:
            print(e)
            return
        prompt_y = input("Move shape by (y) (-10-10): ")
        try:
            Validators.validate_value(prompt_y, -10, 10)
            y = int(prompt_y)
        except ValueError as e:
            print(e)
            return
        prompt_z = input("Move shape by (z) (-10-10): ")
        try:
            Validators.validate_value(prompt_z, -10, 10)
            z = int(prompt_z)
        except ValueError as e:
            print(e)
            return
        self.ascii.move(x, y, z)
        print("Shape was moved successfully")

    def change_color(self):
        """The UI for changing the shape's color"""
        color_prompt = input("Choose the color of your shape:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "8 - Random\n"
                             "0 - Default\n"
                             "Your choice: ")
        try:
            Validators.validate_color(color_prompt, self)
        except ValueError as e:
            print(e)
            return
        print("Shape's color changed successfully")
