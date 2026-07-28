# Snake Game

A classic Snake game built with Python and Pygame. The player controls a growing snake, collects food to increase the score, and tries to survive without hitting the walls or the snake's own body.

This project recreates the traditional Snake experience with a custom purple, pink, cyan, and black color theme. It focuses on real-time movement, keyboard controls, collision detection, random food generation, scoring, survival time, and game-state management.

## Project Overview

The goal of the game is to collect as much food as possible while keeping the snake alive for as long as possible.

The snake begins as a single block in the center of the screen. The player uses the arrow keys to choose a direction, and the snake continues moving in that direction automatically.

Every piece of food increases the snake's length and adds one point to the score. As the snake grows, the player has less open space and must plan each movement more carefully.

The game ends when the snake touches the edge of the window or collides with its own body. After losing, the final score and survival time remain visible, and the player can immediately start a new game or quit.

## Features

- Classic grid-based Snake gameplay
- Arrow-key movement
- Continuous movement at a controlled frame rate
- Food generated at random grid positions
- Food placement that avoids the snake's body
- Snake growth after collecting food
- Live score displayed on screen
- Live survival timer
- Wall collision detection
- Self-collision detection
- Protection against reversing directly into the snake
- Replay and quit options after game over
- Clean restarts without nested game loops
- Custom purple, pink, cyan, and black color palette

## Technologies Used

- Python
- Pygame
- Python `random` module
- Python `time` module
- Functions and list-based game-state management

## How the Game Works

### 1. Game Window

Pygame creates a `600 × 400` game window with a black background.

The game uses four main colors:

- Black for the background
- Purple for the snake
- Pink for the food and game-over messages
- Cyan for the score and timer

The snake and food both use a block size of 10 pixels, which keeps every movement aligned to the same grid.

### 2. Snake Movement

The snake begins in the center of the screen and waits for the player to press an arrow key.

Each key press changes the snake's horizontal or vertical movement:

- Left moves the snake 10 pixels to the left
- Right moves the snake 10 pixels to the right
- Up moves the snake 10 pixels upward
- Down moves the snake 10 pixels downward

The game prevents the snake from instantly reversing direction. For example, a snake moving horizontally cannot switch directly from left to right. The player must first turn vertically.

### 3. Snake Body

The snake's body is stored as a list of coordinate pairs. During every frame, the new head position is added to the list.

If the snake has not collected food, the oldest body position is removed. This makes the snake appear to move without changing its length.

After food is collected, the oldest segment remains in the list, causing the snake to grow.

### 4. Food Generation

Food appears at a random location aligned with the game's 10-pixel grid.

Before selecting a position, the game removes every grid space currently occupied by the snake from the available choices. This guarantees that food never appears underneath the snake's body.

### 5. Score and Timer

The score begins at zero and increases by one whenever the snake collects food.

The timer begins when the player presses the first arrow key. It measures the current run using a monotonic clock, which is not affected if the computer's system time changes.

The score is displayed in the upper-left corner, while the survival time is displayed in the upper-right corner.

### 6. Collision Detection

The game checks for two types of collisions:

- **Wall collision:** The snake's head moves outside the game window
- **Self-collision:** The snake's head reaches a position already occupied by its body

Either collision ends the current run. The final score and time remain frozen on the screen so the player can see the result.

### 7. Restarting or Quitting

After a collision, the game displays:

```text
You Lost!
Press C to Play Again or Q to Quit
```

Pressing `C` starts a completely new game with a one-block snake, a score of zero, and a reset timer. Pressing `Q` closes the game.

## Controls

| Key | Action |
| --- | --- |
| `Left Arrow` | Move left |
| `Right Arrow` | Move right |
| `Up Arrow` | Move up |
| `Down Arrow` | Move down |
| `C` after losing | Play again |
| `Q` after losing | Quit |
| Close window | Quit the game |

## Requirements

- Python 3.x
- Pygame

## Installation

Clone or download the project, then open a terminal inside the project folder.

Install Pygame:

```powershell
python -m pip install pygame
```

## Running the Game

Run the Python file:

```powershell
python snake_game.py
```

The game window will open immediately. Press any arrow key to begin moving and start the timer.

## Project Structure

```text
snake/
├── snake_game.py    Main game file
├── README.md        Project documentation
└── .gitignore       Files and folders excluded from Git
```

## Game Loop

The main game loop follows this process:

```text
Start Game
    |
    v
Create Snake and Food
    |
    v
Wait for the First Direction
    |
    v
Read Keyboard and Window Events
    |
    v
Update the Snake's Position and Timer
    |
    v
Check Wall and Self Collisions
    |
    v
Draw the Food, Snake, Score, and Time
    |
    v
Check Whether Food Was Collected
    |
    v
Repeat at 15 FPS
```

## What I Learned

This project strengthened my understanding of how a real-time game uses a continuous loop to read keyboard input, update object positions, check game rules, and redraw the screen.

I learned how a list of coordinates can represent a moving snake. Adding a new head position and removing the oldest position creates movement, while keeping the oldest segment after collecting food causes the snake to grow. This helped me understand how simple data structures can create visible game behavior.

I also learned how important grid alignment is in a Snake game. Because the snake and food both use 10-pixel positions, their coordinates can match exactly when food is collected. Keeping every object on the same grid makes movement and collision checks easier to manage.

Generating food taught me how random values can be combined with validation. A random position is not automatically a valid position, so the game only selects from spaces that are not occupied by the snake.

The direction checks helped me understand how to prevent invalid player actions. Stopping the snake from immediately reversing direction avoids an instant collision with its own body and makes the controls behave like the original Snake game.

Adding the survival timer showed me how real-world elapsed time can be measured independently of the game's frame count. This keeps the timer accurate even if the frame rate changes slightly.

Finally, this project gave me more experience with game-over states, replay logic, score tracking, frame-rate control, and collision detection. All of these systems work together to turn a small amount of code into a complete playable game.

## Future Improvements

Some improvements I would like to explore include:

- Increase the snake's speed as the score grows
- Save and display a high score
- Add a pause menu
- Add sound effects for collecting food and losing
- Create multiple food types with different point values
- Add obstacles or maze-style levels
- Include difficulty settings
- Replace simple rectangles with custom sprites
- Add smooth animations and visual effects
- Show a separate results screen after each run
- Support WASD controls
- Add a countdown before each new game
- Package the project as a standalone executable

## Troubleshooting

### Pygame is not installed

If the program displays `ModuleNotFoundError: No module named 'pygame'`, install the dependency:

```powershell
python -m pip install pygame
```

### The snake does not move

The snake waits for its first direction. Click the game window to give it keyboard focus, then press one of the arrow keys.

### The game closes immediately

Run the project from a terminal so any error message remains visible:

```powershell
python snake_game.py
```

### The snake will not reverse direction

This is intentional. A snake moving horizontally must turn up or down before it can move in the opposite horizontal direction. The same rule applies to vertical movement.

## License

This project is open source and available for learning, practice, and modification.
