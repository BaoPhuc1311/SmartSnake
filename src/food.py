import random

class Food:
    def __init__(self, width, height, cell_size, get_obstacles_func, get_snake_body_func=None):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.get_obstacles = get_obstacles_func
        self.get_snake_body = get_snake_body_func
        self.position = (0, 0)
        self.spawn_new_food()

    def generate_valid_positions(self):
        all_positions = []
        for x in range(90, 481, self.cell_size):
            for y in range(90, 301, self.cell_size):
                all_positions.append((x, y))
        
        obstacles = self.get_obstacles()
        snake_body = self.get_snake_body() if self.get_snake_body else []
        
        valid_positions = [pos for pos in all_positions if pos not in obstacles and pos not in snake_body]
        return valid_positions

    def spawn_new_food(self):
        obstacles = self.get_obstacles()
        snake_body = self.get_snake_body() if self.get_snake_body else []
        
        valid_positions = self.generate_valid_positions()
        
        if not valid_positions:
            self.position = (90, 90)
            return
        
        self.position = random.choice(valid_positions)
        while self.position in obstacles or self.position in snake_body:
            if not valid_positions:
                self.position = (90, 90)
                break
            self.position = random.choice(valid_positions)

    def get_position(self):
        return self.position
