from Data.Lab5.BLL.classes.shape import Shape


class Cube(Shape):
    def create_shape(self):
        shape = self.create_array(self.size, self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    shape[i][j][k] = "*"
        return shape

    def to_2d(self):
        shape = self.shape
        z_size = len(shape)
        z_offset = max(0, -self.pos_z)
        z_size_normalized = z_size - abs(self.pos_z)
        parts = max(1, 3 * (z_size_normalized // 5))
        increment = max(1, z_size_normalized // parts)
        grid_size = (z_size_normalized + increment - 1) // increment - 1
        result = [[" " for _ in range(len(shape[0][0]) + grid_size + z_offset)]
                  for _ in range(len(shape[0]) + grid_size + z_offset)]
        offset = z_offset
        char = "*"
        num = offset + 1
        for i in range(offset, offset + z_size_normalized, increment):
            row_index = len(result) - 1 - offset
            for j, row in enumerate(reversed(shape[i])):
                col_index = offset
                for k, cell in enumerate(row):
                    if result[row_index][col_index] == " " and cell == "*":
                        result[row_index][col_index] = str(num) if self.debug else char
                    col_index += 1
                row_index -= 1
            offset += 1
            num += 1
            char = "#"
        return result