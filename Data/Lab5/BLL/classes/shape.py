"""An abstract shape to be used by other shape classes"""
from abc import ABC, abstractmethod
import random


class Shape(ABC):
    """An abstract shape class"""
    def __init__(self, size, color="\033[39m", debug=False):
        self.size = size
        self.shape = self.create_shape()
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.color = "\033[" + str(random.randint(31, 39)) + "m" if color == "random" else color
        self.debug = debug

    def __str__(self):
        result = [self.color]
        shape_2d = self.to_2d()
        for i in shape_2d:
            for j in i:
                result.append(str(j))
            result.append("\n")
        result.pop()
        result.append("\033[0m")
        return "".join(result)

    def __repr__(self):
        result = []
        shape_2d = self.to_2d()
        for i in shape_2d:
            for j in i:
                result.append(str(j))
            result.append("\n")
        return "".join(result)


    @abstractmethod
    def create_shape(self):
        """Creates a shape object"""

    @abstractmethod
    def to_2d(self):
        """Transforms the shape into a 2D string array"""

    @staticmethod
    def create_array(width, height):
        """Creates an array for the shape"""
        shape = [[[" " for _ in range(width)] for _ in range(height)] for _ in range(width)]
        return shape

    def change_size(self, new_size):
        """Changes the size of the shape"""
        self.size = new_size
        self.shape = self.create_shape()
        if self.pos_x != 0 or self.pos_y != 0 or self.pos_z != 0:
            self.move()

    def move(self, x=0, y=0, z=0):
        """Moves the shape by the specified value."""
        self.pos_x += x
        self.pos_y += y
        self.pos_z += z

        shape = self.create_shape()
        size_x = len(shape[0][0])
        size_y = len(shape[0])

        def add_empty_layers(s, x_size, y_size, z_shift):
            """Adds empty layers to the shape along the Z-axis."""
            for _ in range(abs(z_shift)):
                empty_layer = [[" " for _ in range(x_size)] for _ in range(y_size)]
                if z_shift > 0:
                    s.append(empty_layer)
                else:
                    s.insert(0, empty_layer)
            return s

        def add_empty_rows(s, x_size, y_shift):
            """Adds empty rows to the shape along the Y-axis."""
            for layer in s:
                for _ in range(abs(y_shift)):
                    empty_row = [" " for _ in range(x_size)]
                    if y_shift > 0:
                        layer.append(empty_row)
                    else:
                        layer.insert(0, empty_row)
            return s

        def add_empty_columns(s, x_shift):
            """Adds empty columns to the shape along the X-axis."""
            for layer in s:
                for row in layer:
                    for _ in range(abs(x_shift)):
                        if x_shift < 0:
                            row.append(" ")
                        else:
                            row.insert(0, " ")
            return s

        if self.pos_z != 0:
            shape = add_empty_layers(shape, size_x, size_y, self.pos_z)
        if self.pos_y != 0:
            shape = add_empty_rows(shape, size_x, self.pos_y)
        if self.pos_x != 0:
            shape = add_empty_columns(shape, self.pos_x)

        self.shape = shape
