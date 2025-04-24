class Snake:
    def __init__(self, start_pos, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        x, y = start_pos
        self.body = [
            (x, y),
            (x - cell_size, y)
        ]
        self.direction = (cell_size, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if (new_head[0] < 0 or new_head[0] >= self.width or
            new_head[1] < 0 or new_head[1] >= self.height):
            return False

        if new_head in self.body[1:]:
            return False

        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def set_direction(self, new_direction):
        dir_x, dir_y = self.direction
        new_dir_x, new_dir_y = new_direction
        if (dir_x, dir_y) != (-new_dir_x, -new_dir_y):
            self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1])

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body
