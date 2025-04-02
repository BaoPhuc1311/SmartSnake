import random

class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, self.screen_width, self.cell_size)
        y = random.randrange(0, self.screen_height, self.cell_size)
        return (x, y)

    def get_position(self):
        return self.position

    def spawn_new_food(self):
        self.position = self.random_position()
