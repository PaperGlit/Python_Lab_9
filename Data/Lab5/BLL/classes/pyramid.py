"""A pyramid shape"""
from Data.Lab5.BLL.classes.shape import Shape


class Pyramid(Shape):
    """A pyramid shape class"""
    def create_shape(self):
        """Creates a pyramid shape"""
        width = self.size * 2 - 1
        shape = self.create_array(width, self.size)
        start = self.size
        end = self.size
        for i in range(self.size):
            for j in range(start - 1, end):
                for k in range(start - 1, end):
                    shape[j][i][k] = "*"
            start -= 1
            end += 1
        final_shape = [[[shape[z][x][y] for z in range(len(shape))]
                        for x in range(len(shape[0]))] for y in range(len(shape[0][0]))]
        return final_shape

    def to_2d(self):
        """Transforms the pyramid into a 2D string array"""
        shape = self.shape
        z_offset = max(0, -self.pos_z)
        depth = len(shape)
        height = len(shape[0])
        width = len(shape[0][0])
        result = [[" " for _ in range(width + 1 + z_offset)] for _ in range(height + 1 + z_offset)]
        midpoint = (depth - abs(self.pos_z) - 1) // 2 + z_offset
        char = "*"
        num = 1
        for offset in range(z_offset, z_offset + 2, 1):
            i1 = len(result) - 1 - offset
            for i in reversed(range(height)):
                j1 = offset
                for j in range(width):
                    if result[i1][j1] == " " and shape[midpoint][i][j] == "*" and not self.debug:
                        result[i1][j1] = char
                    elif result[i1][j1] == " " and shape[midpoint][i][j] == "*" and self.debug:
                        result[i1][j1] = num
                    j1 += 1
                i1 -= 1
            char = "#"
            num += 1
        return result
