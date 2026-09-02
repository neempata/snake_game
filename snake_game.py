import random
import time
import pygame

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

# Display settings
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 500

# Snake settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Create the game window
DIS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the game clock and fonts
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bitstreamverasans", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


def draw_hud(score, elapsed_time):
    """Display the current score and survival time."""
    score_text = score_font.render(f"Score: {score}", True, CYAN)
    time_text = score_font.render(f"Time: {elapsed_time:.1f}s", True, CYAN)

    DIS.blit(score_text, (10, 5))
    DIS.blit(
        time_text,
        (DISPLAY_WIDTH - time_text.get_width() - 10, 5),
    )


def draw_snake(snake_list):
    """Draw every block of the snake."""
    for x_position, y_position in snake_list:
        pygame.draw.rect(
            DIS,
            PURPLE,
            (x_position, y_position, SNAKE_BLOCK, SNAKE_BLOCK),
        )


def draw_centered_message(text, color, y_position):
    """Draw a message centered horizontally on the screen."""
    message_surface = font_style.render(text, True, color)
    message_rectangle = message_surface.get_rect(
        center=(DISPLAY_WIDTH // 2, y_position)
    )
    DIS.blit(message_surface, message_rectangle)


def random_food_position(snake_list):
    """Choose a free grid position that is not occupied by the snake."""
    occupied_positions = {tuple(position) for position in snake_list}
    available_positions = [
        (x_position, y_position)
        for x_position in range(0, DISPLAY_WIDTH, SNAKE_BLOCK)
        for y_position in range(0, DISPLAY_HEIGHT, SNAKE_BLOCK)
        if (x_position, y_position) not in occupied_positions
    ]

    if not available_positions:
        return None

    return random.choice(available_positions)


def game_loop():
    """Run one complete game and return True when the player wants a replay."""
    snake_x = DISPLAY_WIDTH // 2
    snake_y = DISPLAY_HEIGHT // 2
    x_change = 0
    y_change = 0

    snake_list = [[snake_x, snake_y]]
    score = 0
    food_position = random_food_position(snake_list)

    started_at = None
    final_time = 0.0
    game_over = False
    player_won = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_q:
                        return False
                    if event.key == pygame.K_c:
                        return True
                else:
                    direction_changed = False

                    if event.key == pygame.K_LEFT and x_change == 0:
                        x_change = -SNAKE_BLOCK
                        y_change = 0
                        direction_changed = True
                    elif event.key == pygame.K_RIGHT and x_change == 0:
                        x_change = SNAKE_BLOCK
                        y_change = 0
                        direction_changed = True
                    elif event.key == pygame.K_UP and y_change == 0:
                        y_change = -SNAKE_BLOCK
                        x_change = 0
                        direction_changed = True
                    elif event.key == pygame.K_DOWN and y_change == 0:
                        y_change = SNAKE_BLOCK
                        x_change = 0
                        direction_changed = True

                    if direction_changed and started_at is None:
                        started_at = time.monotonic()

        if started_at is None:
            elapsed_time = 0.0
        elif game_over:
            elapsed_time = final_time
        else:
            elapsed_time = time.monotonic() - started_at

        if not game_over and started_at is not None:
            next_x = snake_x + x_change
            next_y = snake_y + y_change

            hit_wall = (
                next_x < 0
                or next_x >= DISPLAY_WIDTH
                or next_y < 0
                or next_y >= DISPLAY_HEIGHT
            )

            if hit_wall:
                game_over = True
                final_time = elapsed_time
            else:
                new_head = [next_x, next_y]
                ate_food = (
                    food_position is not None
                    and (next_x, next_y) == food_position
                )

                # The tail moves away when the snake is not growing, so moving
                # into the tail's previous position is a legal move.
                body_to_check = snake_list if ate_food else snake_list[1:]

                if new_head in body_to_check:
                    game_over = True
                    final_time = elapsed_time
                else:
                    snake_x = next_x
                    snake_y = 
                    snake_list.append(new_head)

                    if ate_food:
                        score += 1
                        food_position = random_food_position(snake_list)

                        if food_position is None:
                            player_won = True
                            game_over = True
                            final_time = elapsed_time
                    else:
                        snake_list.pop(0)

        DIS.fill(BLACK)

        if food_position is not None:
            pygame.draw.rect(
                DIS,
                PINK,
                (
                    food_position[0],
                    food_position[1],
                    SNAKE_BLOCK,
                    SNAKE_BLOCK,
                ),
            )

        draw_snake(snake_list)
        draw_hud(score, elapsed_time)

        if started_at is None:
            draw_centered_message(
                "Press an arrow key to start",
                WHITE,
                DISPLAY_HEIGHT // 3,
            )

        if game_over:
            result_message = "You Won!" if player_won else "You Lost!"
            draw_centered_message(
                result_message,
                PINK,
                DISPLAY_HEIGHT // 3,
            )
            draw_centered_message(
                "Press C to Play Again or Q to Quit",
                PINK,
                DISPLAY_HEIGHT // 3 + 40,
            )

        pygame.display.update()
        clock.tick(SNAKE_SPEED)


def main():
    """Run new rounds until the player quits."""
    play_again = True

    while play_again:
        play_again = game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
