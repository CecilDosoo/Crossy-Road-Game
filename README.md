# Crossy Road Game

This project is a Python program that simulates the Crossy Road game using the Turtle module. The game is structured across multiple Python files, each handling different aspects of the game. The game includes classes for managing the player, obstacles (cars), and the scoreboard, creating a cohesive and interactive game experience.

## Game Overview

The game involves a player navigating a character across the screen while avoiding moving cars. The player's progress is tracked, and the game features levels that increase in difficulty over time.

## Screenshots

https://github.com/user-attachments/assets/aeedee0d-2ac6-4f7e-bb4d-5094fd91c60b

![Game Screenshot 1](https://github.com/user-attachments/assets/a48c6389-3d43-4e50-bf2f-9f3807ca6346)
![Game Screenshot 2](https://github.com/user-attachments/assets/87300a3c-6d9c-45f3-b9b8-46e28e210415)
![Game Screenshot 3](https://github.com/user-attachments/assets/0f5bf13f-7ae1-4d2a-a8d9-1e1a18efc795)

## Components

### CarManager

The `CarManager` class handles the creation and movement of cars, which are the primary obstacles in the game.

- **`create_cars()`**: Randomly generates cars with a 1 in 6 chance of appearing. Each car is a rectangular shape with a random color and is positioned at a random y-coordinate along the right edge of the screen.
  
- **`move()`**: Moves all cars from right to left across the screen at a constant speed.
  
- **`move_faster()`**: Increases the speed of all cars, making them move faster by adding an increment to their movement distance. This enables dynamic gameplay with increasing difficulty.

### Player

The `Player` class represents the player’s character in the game.

- **Initialization**: The player character is a turtle with a specific shape, white color, and starting position at the bottom center of the screen. It is oriented to face upwards, simulating movement towards the top of the screen.
  
- **`move()`**: Moves the turtle forward by a fixed distance, simulating progress towards the finish line.
  
- **`reset_position()`**: Resets the turtle to its starting position, typically after reaching the finish line.

### Scoreboard

The `Scoreboard` class manages the display of the player's level and game-over message.

- **Initialization**: The scoreboard is a hidden turtle positioned at the top left of the screen. It starts by displaying the initial level, set to 1, using a predefined font.
  
- **`level_increase()`**: Updates the level on the screen by clearing the previous level display, incrementing the level, and writing the new level.
  
- **`game_over()`**: Displays a "GAME OVER" message at the center of the screen when the game ends, signaling the player that the game is over.

## How to Run

To run the game, make sure you have Python installed on your system. Execute the main Python script that initializes the game and starts the Turtle graphics window.
