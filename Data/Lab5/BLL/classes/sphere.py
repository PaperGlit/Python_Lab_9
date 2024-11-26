"""A sphere shape"""
from Data.Lab5.BLL.classes.shape import Shape


class Sphere(Shape):
    """A sphere shape class"""
    def create_shape(self):
        """Creates a sphere shape"""
        shape = self.create_array(self.size, self.size)
        center = (self.size + 1) // 2
        if self.size % 2 == 0:
            up_part = list(range(center + 1, self.size + 1))
            cycle = up_part + up_part[::-1]
        else:
            up_part = list(range(center, self.size + 1))
            cycle = up_part + up_part[-2::-1]
        j = 0
        for i in cycle:
            if i >= 1:
                shape[j] = self.create_circle(i)
            j += 1
        final_shape = [[[shape[z][y][x] for x in range(self.size)]
                        for y in range(self.size)] for z in range(self.size) ]
        return final_shape

    def create_circle(self, diameter):
        """Creates a circle shape"""
        result = [[" " for _ in range(diameter)] for _ in range(diameter)]
        radius = diameter / 2 - .5
        r = (radius + .25) ** 2 + 1
        for i in range(diameter):
            y = (i - radius) ** 2
            for j in range(diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result[i][j] = "*"
                else:
                    result[i][j] = " "
        return self.expand_array(result)

    def expand_array(self, array2):
        """Expands an array"""
        array1 = [[" " for _ in range(self.size)] for _ in range(self.size)]
        expand_start = (len(array1) - len(array2)) // 2
        expand_end = self.size - expand_start if (
                (len(array1) - len(array2)) % 2 == 0) else self.size - expand_start - 1
        i1, j1 = 0, 0
        for i in range(expand_start, expand_end):
            for j in range(expand_start, expand_end):
                array1[i][j] = array2[i1][j1]
                j1 += 1
            j1 = 0
            i1 += 1
        return array1

    def to_2d(self):
        """Transforms the sphere into a 2D string array"""
        shape = self.shape
        z_offset = max(0, -self.pos_z)
        depth = len(shape)
        height = len(shape[0])
        width = len(shape[0][0])
        result = [[" " for _ in range(width + z_offset)] for _ in range(height + z_offset)]
        chars = ["#", "*", "%", "@"]
        char = 0
        num = 1
        for i in range(depth):
            for j in range(height):
                for k in range(width):
                    if result[j][k + z_offset] == " " and shape[i][j][k] == "*" and not self.debug:
                        result[j][k + z_offset] = chars[char]
                    elif result[j][k + z_offset] == " " and shape[i][j][k] == "*" and self.debug:
                        result[j][k + z_offset] = num
            char = 0 if char == len(chars) - 1 else char + 1
            num += 1
        return result
