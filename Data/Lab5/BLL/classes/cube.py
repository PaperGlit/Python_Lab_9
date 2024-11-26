"""A cube shape"""
from Data.Lab5.BLL.classes.shape import Shape


class Cube(Shape):
    """A cube shape class"""
    def create_shape(self):
        """Creates a cube shape"""
        shape = self.create_array(self.size, self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    shape[i][j][k] = "*"
        return shape

    def to_2d(self):
        """Transforms the cube into a 2D string array"""
        z_size = len(self.shape)
        z_offset = max(0, -self.pos_z)
        z_size_normalized = z_size - abs(self.pos_z)
        parts = max(1, 3 * (z_size_normalized // 5))
        increment = max(1, z_size_normalized // parts)
        grid_size = (z_size_normalized + increment - 1) // increment - 1
        result = [[" " for _ in range(len(self.shape[0][0]) + grid_size + z_offset)]
                  for _ in range(len(self.shape[0]) + grid_size + z_offset)]
        result = self.print_squares(result, z_offset, z_size_normalized, increment)
        return result

    def print_squares(self, result, z_offset, z_size_normalized, increment):
        """A to_2d() subfunction that does the filling of the result array"""
        offset = z_offset
        char = "*"
        num = offset + 1
        for i in range(offset, offset + z_size_normalized, increment):
            row_index = len(result) - 1 - offset
            for _, row in enumerate(reversed(self.shape[i])):
                col_index = offset
                for _, cell in enumerate(row):
                    if result[row_index][col_index] == " " and cell == "*":
                        result[row_index][col_index] = str(num) if self.debug else char
                    col_index += 1
                row_index -= 1
            offset += 1
            num += 1
            char = "#"
        return result
