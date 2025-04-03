import random

class Food:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = self.generate_random_position()

    def generate_random_position(self):
        x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
        y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
        return (x, y)

    def spawn_new_food(self):
        self.position = self.generate_random_position()

    def get_position(self):
        return self.position
