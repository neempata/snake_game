import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define current colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

# Set display dimensions
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400

# Initialize the game display
DIS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up game clock
clock = pygame.time.Clock()

# Set snake block size and speed
snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont("bitstreamverasans", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_score(score):
    """Display the current score on the screen."""
    value = score_font.render("Score: " + str(score), True, CYAN)
    DIS.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    """Draw the snake on the display."""
    for x in snake_list:
        pygame.draw.rect(DIS, PURPLE, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    DIS.blit(mesg, [DISPLAY_WIDTH / 6, DISPLAY_HEIGHT / 3])

def random_food_position(snake_list):
    """Generate a random position for the food not on the snake."""
    while True:
        foodx = round(random.randrange(0, DISPLAY_WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, DISPLAY_HEIGHT - snake_block) / 10.0) * 10.0
        if [foodx, foody] not in snake_list:
            return foodx, foody

def game_loop():
    """Main game loop for the Snake game."""
    game_over = False
    game_close = False

    x1 = DISPLAY_WIDTH / 2
    y1 = DISPLAY_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = random_food_position(snake_List)

    while not game_over:

        while game_close:
            DIS.fill(BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", PINK)
            draw_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= DISPLAY_WIDTH or x1 < 0 or y1 >= DISPLAY_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLACK)
        pygame.draw.rect(DIS, PINK, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collision with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        draw_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            foodx, foody = random_food_position(snake_List)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
            

                        










# import modules (pygame, time, random)
#init pygame
# define colors
#set display dimensions
#initialize the game display
#set up the clock 
#set snake block size and speed
#font styles
#define your score class
# define the snake class
#def message function to display text
#def game_loop 
  #main game loop
  #initial snake position and direction
  #snake movement logic
  #snake body
  #snake food logic
    #
