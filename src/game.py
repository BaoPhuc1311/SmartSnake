import pygame
from snake import Snake
from food import Food

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 30
WHITE = (255, 255, 255)

def draw_snake(screen, snake):
    for segment in snake.get_body():
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, (255, 0, 0), (*food.get_position(), CELL_SIZE, CELL_SIZE))

def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Snake")

    snake = Snake((100, 100))
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

        if snake.get_head() == food.get_position():
            snake.grow()
            food.spawn_new_food()

    pygame.quit()
