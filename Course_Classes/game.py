import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the snake
snake_size = 10
snake_speed = 15
direction = "right"
snake_list = []
snake_length = 1

# Set up the food
food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

# Set up the score
score_font = pygame.font.SysFont(None, 25)


def message(msg, color):
    msg = score_font.render(msg, True, color)
    window.blit(msg, [window_width / 6, window_height / 3])


def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_size, snake_size])

def draw_food(food_x, food_y, food_size):
    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
    return food_x, food_y

def game_loop():
    global direction

    game_over = False
    game_close = False

    x = window_width / 2
    y = window_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_size = 10
    food_x = round(random.randrange(0, window_width - food_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - food_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            window.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    y_change = snake_size
                    x_change = 0

        # Check for collision with the walls
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_close = True

        # Update the position of the snake
        x += x_change
        y += y_change

        window.fill(white)

        # Draw the food
        draw_food(food_x, food_y, food_size)

        # Draw the snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        pygame.display.update()

        # Check for collision with the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        # Set up the score
        score_text = score_font.render("Score: " + str(snake_length - 1), True, black)
        window.blit(score_text, [0, 0])

        # Update the display
        pygame.display.update()

        # Set the game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Quit pygame and the program
    pygame.quit()
    quit()


