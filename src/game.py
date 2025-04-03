import pygame
from snake import Snake
from food import Food

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 30
WHITE = (255, 255, 255)

DIRECTIONS = {
    pygame.K_UP: (0, -CELL_SIZE),
    pygame.K_DOWN: (0, CELL_SIZE),
    pygame.K_LEFT: (-CELL_SIZE, 0),
    pygame.K_RIGHT: (CELL_SIZE, 0),
    pygame.K_w: (0, -CELL_SIZE),
    pygame.K_s: (0, CELL_SIZE),
    pygame.K_a: (-CELL_SIZE, 0),
    pygame.K_d: (CELL_SIZE, 0)
}

def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def draw_snake(screen, snake):
    for segment in snake.get_body():
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, (255, 0, 0), (*food.get_position(), CELL_SIZE, CELL_SIZE))

def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SmartSnake Game")
    clock = pygame.time.Clock()

    snake = Snake((100, 100), CELL_SIZE, WIDTH, HEIGHT)
    food = Food(WIDTH, HEIGHT, CELL_SIZE)

    running = True
    while running:
        screen.fill(WHITE)
        
        draw_snake(screen, snake)
        draw_food(screen, food)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in DIRECTIONS:
                    snake.set_direction(DIRECTIONS[event.key])

        if not snake.move():
            running = False

        snake_rect = pygame.Rect(*snake.get_head(), CELL_SIZE, CELL_SIZE)
        food_rect = pygame.Rect(*food.get_position(), CELL_SIZE, CELL_SIZE)

        if is_collision(snake_rect, food_rect):
            snake.grow()
            food.spawn_new_food()

        clock.tick(10)

    pygame.quit()
