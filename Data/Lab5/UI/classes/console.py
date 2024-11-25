from Data.Shared.classes.validators import Validators
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class Console:
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Console, self).__call__(*args, **kwargs)
        else:
            self._instances[self].__init__(*args, **kwargs)
        return self._instances[self]

    def __init__(self):
        self.__prompt()
        self.shape = None

    def __prompt(self):
        self.create_shape()
        while True:
            prompt = input("1 - Create a new shape\n"
                           "2 - Change shape's size\n"
                           "3 - Move shape\n"
                           "4 - Change shape's color\n"
                           "5 - Print shape\n"
                           "Your choice: ")
            try:
                Validators.main_prompt(prompt, self)
            except ValueError:
                return

    def create_shape(self):
        while True:
            shape_prompt = input("Select shape:\n"
                           "1 - Cube\n"
                           "2 - Pyramid\n"
                           "3 - Sphere\n"
                           "Your choice: ")
            try:
                shape = Validators.validate_value(shape_prompt, 0, 4)
            except ValueError as e:
                print(e)
                continue
            size_prompt = input("Enter shape's size (5-100): ")
            try:
                size = Validators.validate_value(size_prompt, 4, 101)
            except ValueError as e:
                print(e)
                continue
            self.shape = Validators.create_shape(shape, size)
            print("Shape was created successfully")
            return

    def change_size(self):
        prompt = input("Change shape's new size (5-100): ")
        try:
            size = Validators.validate_value(prompt, 4, 101)
        except ValueError as e:
            print(e)
            return
        self.shape.change_size(size)
        print("Shape's size was changed successfully")

    def move_shape(self):
        prompt_x = input("Move shape by (x) (-10-10): ")
        try:
            x = Validators.validate_value(prompt_x, -10, 10)
        except ValueError as e:
            print(e)
            return
        prompt_y = input("Move shape by (y) (-10-10): ")
        try:
            y = Validators.validate_value(prompt_y, -10, 10)
        except ValueError as e:
            print(e)
            return
        prompt_z = input("Move shape by (z) (-10-10): ")
        try:
            z = Validators.validate_value(prompt_z, -10, 10)
        except ValueError as e:
            print(e)
            return
        self.shape.move(x, y, z)
        print("Shape was moved successfully")

    def change_color(self):
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