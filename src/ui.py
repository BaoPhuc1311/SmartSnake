import pygame
from snake import Snake
from food import Food

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

def get_head_direction(snake):
    dir_x, dir_y = snake.direction
    if dir_x == CELL_SIZE:
        return "right"
    elif dir_x == -CELL_SIZE:
        return "left"
    elif dir_y == -CELL_SIZE:
        return "up"
    elif dir_y == CELL_SIZE:
        return "down"
    return "right"

def get_body_image(segment, prev_segment, next_segment, images):
    prev_x, prev_y = prev_segment
    curr_x, curr_y = segment
    next_x, next_y = next_segment

    from_prev = (curr_x - prev_x, curr_y - prev_y)
    to_next = (next_x - curr_x, next_y - curr_y)

    if to_next == (0, 0):
        return images["body_horizontal"]

    if from_prev == to_next:
        if from_prev[0] != 0:
            return images["body_horizontal"]
        else:
            return images["body_vertical"]

    if from_prev == (0, -CELL_SIZE) and to_next == (CELL_SIZE, 0):
        return images["body_topright"]
    elif from_prev == (0, -CELL_SIZE) and to_next == (-CELL_SIZE, 0):
        return images["body_topleft"]
    elif from_prev == (0, CELL_SIZE) and to_next == (CELL_SIZE, 0):
        return images["body_bottomright"]
    elif from_prev == (0, CELL_SIZE) and to_next == (-CELL_SIZE, 0):
        return images["body_bottomleft"]
    elif from_prev == (-CELL_SIZE, 0) and to_next == (0, -CELL_SIZE):
        return images["body_topleft"]
    elif from_prev == (-CELL_SIZE, 0) and to_next == (0, CELL_SIZE):
        return images["body_bottomleft"]
    elif from_prev == (CELL_SIZE, 0) and to_next == (0, -CELL_SIZE):
        return images["body_topright"]
    elif from_prev == (CELL_SIZE, 0) and to_next == (0, CELL_SIZE):
        return images["body_bottomright"]

    return images["body_horizontal"]

def get_tail_direction(tail, prev_segment):
    tail_x, tail_y = tail
    prev_x, prev_y = prev_segment
    dir_x, dir_y = tail_x - prev_x, tail_y - prev_y
    if dir_x == CELL_SIZE:
        return "right"
    elif dir_x == -CELL_SIZE:
        return "left"
    elif dir_y == -CELL_SIZE:
        return "up"
    elif dir_y == CELL_SIZE:
        return "down"
    return "right"

def draw_snake(screen, snake, images):
    snake_body = snake.get_body()

    head_direction = get_head_direction(snake)
    head_img = images[f"head_{head_direction}"]
    screen.blit(head_img, snake_body[0])

    if len(snake_body) == 1:
        return

    if len(snake_body) == 2:
        tail = snake_body[-1]
        prev_segment = snake_body[-2]
        tail_direction = get_tail_direction(tail, prev_segment)
        tail_img = images[f"tail_{tail_direction}"]
        screen.blit(tail_img, tail)
        return

    for i in range(1, len(snake_body) - 1):
        segment = snake_body[i]
        prev_segment = snake_body[i - 1]
        next_segment = snake_body[i + 1]

        prev_x, prev_y = prev_segment
        curr_x, curr_y = segment
        next_x, next_y = next_segment
        from_prev = (curr_x - prev_x, curr_y - prev_y)
        to_next = (next_x - curr_x, next_y - curr_y)

        if to_next == (0, 0):
            body_img = images["body_horizontal"]
        else:
            body_img = get_body_image(segment, prev_segment, next_segment, images)
        screen.blit(body_img, segment)

    tail = snake_body[-1]
    prev_segment = snake_body[-2]
    tail_direction = get_tail_direction(tail, prev_segment)
    tail_img = images[f"tail_{tail_direction}"]
    screen.blit(tail_img, tail)

def draw_food(screen, food, food_img):
    screen.blit(food_img, food.get_position())

def draw_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def draw_game_over(screen, score, font):
    game_over_text = font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    restart_text = font.render("Press R to Restart", True, BLACK)
    
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

def draw_pause_screen(screen, font):
    pause_text = font.render("Game Paused - Press P to Resume", True, BLACK)
    screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

def draw_menu(screen, font, selected_mode):
    menu_bg = pygame.Surface((WIDTH, HEIGHT))
    menu_bg.set_alpha(200)
    menu_bg.fill(WHITE)
    screen.blit(menu_bg, (0, 0))
    
    title_text = font.render("SmartSnake", True, BLACK)
    human_text = font.render("Human Mode", True, BLACK if selected_mode == "human" else (150, 150, 150))
    ai_text = font.render("AI Mode", True, BLACK if selected_mode == "ai" else (150, 150, 150))
    start_text = font.render("Press Enter to Start", True, BLACK)
    
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(human_text, (WIDTH // 2 - human_text.get_width() // 2, HEIGHT // 2 - 30))
    screen.blit(ai_text, (WIDTH // 2 - ai_text.get_width() // 2, HEIGHT // 2 + 10))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 80))

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SmartSnake Game")
    clock = pygame.time.Clock()

    images = {
        "head_up": pygame.image.load("assets/images/head_up.png").convert_alpha(),
        "head_down": pygame.image.load("assets/images/head_down.png").convert_alpha(),
        "head_left": pygame.image.load("assets/images/head_left.png").convert_alpha(),
        "head_right": pygame.image.load("assets/images/head_right.png").convert_alpha(),
        "body_horizontal": pygame.image.load("assets/images/body_horizontal.png").convert_alpha(),
        "body_vertical": pygame.image.load("assets/images/body_vertical.png").convert_alpha(),
        "body_topleft": pygame.image.load("assets/images/body_topleft.png").convert_alpha(),
        "body_topright": pygame.image.load("assets/images/body_topright.png").convert_alpha(),
        "body_bottomleft": pygame.image.load("assets/images/body_bottomleft.png").convert_alpha(),
        "body_bottomright": pygame.image.load("assets/images/body_bottomright.png").convert_alpha(),
        "tail_up": pygame.image.load("assets/images/tail_up.png").convert_alpha(),
        "tail_down": pygame.image.load("assets/images/tail_down.png").convert_alpha(),
        "tail_left": pygame.image.load("assets/images/tail_left.png").convert_alpha(),
        "tail_right": pygame.image.load("assets/images/tail_right.png").convert_alpha(),
    }
    food_img = pygame.image.load("assets/images/apple.png").convert_alpha()
    start_background = pygame.image.load("assets/images/start_game.png").convert()
    game_background = pygame.image.load("assets/images/background.png").convert()
    
    font = pygame.font.SysFont("Arial", 24)

    snake = Snake((100, 100), CELL_SIZE, WIDTH, HEIGHT)
    food = Food(WIDTH, HEIGHT, CELL_SIZE)
    score = 0
    game_over = False
    game_started = False
    paused = False
    game_mode = "human"
    selected_mode = "human"

    running = True
    while running:
        if not game_started:
            screen.blit(start_background, (0, 0))
        else:
            screen.blit(game_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_started:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        selected_mode = "ai" if selected_mode == "human" else "human"
                    elif event.key == pygame.K_RETURN:
                        game_started = True
                        game_mode = selected_mode
                        screen.blit(game_background, (0, 0))
                        pygame.display.flip()
                elif game_over:
                    if event.key == pygame.K_r:
                        snake = Snake((100, 100), CELL_SIZE, WIDTH, HEIGHT)
                        food = Food(WIDTH, HEIGHT, CELL_SIZE)
                        score = 0
                        game_over = False
                        paused = False
                        screen.blit(game_background, (0, 0))
                        pygame.display.flip()
                else:
                    if event.key == pygame.K_p:
                        paused = not paused
                    elif game_mode == "human" and event.key in DIRECTIONS and not paused:
                        snake.set_direction(DIRECTIONS[event.key])

        if not game_started:
            draw_menu(screen, font, selected_mode)
        else:
            if not game_over:
                if not paused:
                    if game_mode == "ai":
                        pass
                    else:
                        if not snake.move():
                            game_over = True

                    snake_rect = pygame.Rect(*snake.get_head(), CELL_SIZE, CELL_SIZE)
                    food_rect = pygame.Rect(*food.get_position(), CELL_SIZE, CELL_SIZE)

                    if is_collision(snake_rect, food_rect):
                        snake.grow()
                        food.spawn_new_food()
                        score += 10

                draw_snake(screen, snake, images)
                draw_food(screen, food, food_img)
                draw_score(screen, score, font)

                if paused:
                    draw_pause_screen(screen, font)
            else:
                draw_game_over(screen, score, font)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
