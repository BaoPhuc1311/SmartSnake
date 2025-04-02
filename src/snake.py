class Snake:
    def __init__(self, initial_position):
        self.body = [initial_position]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail_x, tail_y = self.body[-1]
        new_tail = (tail_x - self.direction[0], tail_y - self.direction[1])
        self.body.append(new_tail)

    def change_direction(self, new_direction):
        self.direction = new_direction

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body
