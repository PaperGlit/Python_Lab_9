from abc import ABC, abstractmethod
import random


class Shape(ABC):
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

    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def to_2d(self):
        pass

    @staticmethod
    def create_array(width, height):
        shape = [[[" " for _ in range(width)] for _ in range(height)] for _ in range(width)]
        return shape

    def change_size(self, new_size):
        self.size = new_size
        self.shape = self.create_shape()
        if self.pos_x != 0 or self.pos_y != 0 or self.pos_z != 0:
            self.move()

    def move(self, x=0, y=0, z=0):
        self.pos_x += x
        self.pos_y += y
        self.pos_z += z
        shape = self.create_shape()
        size_x = len(shape[0][0])
        size_y = len(shape[0])
        size_z = len(shape)
        if self.pos_z != 0:
            for _ in range(abs(self.pos_z)):
                empty_layer = [[" " for _ in range (size_x)] for _ in range(size_y)]
                shape.append(empty_layer) if self.pos_z > 0 else shape.insert(0, empty_layer)
            size_z = len(shape)
        if self.pos_y != 0:
            for i in range(size_z):
                for _ in range(abs(self.pos_y)):
                    empty_row = [" " for _ in range (size_x)]
                    shape[i].append(empty_row) if self.pos_y > 0 else shape[i].insert(0, empty_row)
                size_y = len(shape[i])
        if self.pos_x != 0:
            for i in range(size_z):
                for j in range(size_y):
                    for _ in range(abs(self.pos_x)):
                        shape[i][j].append(" ") if self.pos_x < 0 else shape[i][j].insert(0, " ")
        self.shape = shape