import random
import math

class Obstacle:
    def __init__(self, width, height, cell_size, get_snake_head_func, food_position=None):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.get_snake_head = get_snake_head_func
        self.food_position = food_position
        self.obstacles = []
        self.add_border_obstacles()
        self.add_middle_obstacles()

    def add_border_obstacles(self):
        for x in range(0, self.width, self.cell_size):
            self.obstacles.append((x, 0))
            self.obstacles.append((x, self.height - self.cell_size))
        for y in range(0, self.height, self.cell_size):
            self.obstacles.append((0, y))
            self.obstacles.append((self.width - self.cell_size, y))

    def add_middle_obstacles(self):
        possible_positions = []
        for x in range(90, 481, self.cell_size):
            for y in range(90, 301, self.cell_size):
                possible_positions.append((x, y))

        possible_positions = [pos for pos in possible_positions if pos not in self.obstacles]

        for _ in range(5):
            if not possible_positions:
                break
            snake_head = self.get_snake_head()
            valid_positions = []
            for pos in possible_positions:
                distance_to_snake = math.sqrt((pos[0] - snake_head[0])**2 + (pos[1] - snake_head[1])**2)
                distance_to_food = float('inf')
                if self.food_position:
                    food_x, food_y = self.food_position
                    distance_to_food = math.sqrt((pos[0] - food_x)**2 + (pos[1] - food_y)**2)
                min_distance_to_obstacles = float('inf')
                for obstacle in self.obstacles:
                    if obstacle in [(x, 0) for x in range(0, self.width, self.cell_size)] or \
                       obstacle in [(x, self.height - self.cell_size) for x in range(0, self.width, self.cell_size)] or \
                       obstacle in [(0, y) for y in range(0, self.height, self.cell_size)] or \
                       obstacle in [(self.width - self.cell_size, y) for y in range(0, self.height, self.cell_size)]:
                        continue
                    obs_x, obs_y = obstacle
                    distance = math.sqrt((pos[0] - obs_x)**2 + (pos[1] - obs_y)**2)
                    min_distance_to_obstacles = min(min_distance_to_obstacles, distance)

                if (distance_to_snake >= 300 and
                    distance_to_food >= 90 and
                    min_distance_to_obstacles >= 90):
                    valid_positions.append(pos)
            
            if not valid_positions:
                continue
                
            new_obstacle = random.choice(valid_positions)
            self.obstacles.append(new_obstacle)
            possible_positions = [
                pos for pos in possible_positions
                if math.sqrt((pos[0] - new_obstacle[0])**2 + (pos[1] - new_obstacle[1])**2) >= 90
            ]

    def get_obstacles(self):
        return self.obstacles
