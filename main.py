import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    # Detect when turtle collides with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when turtle has reached the top
    if player.ycor() > 280:
        scoreboard.level_increase()
        car_manager.move_faster()
        player.reset_position()


screen.exitonclick()


######READ ME
#Developed the crossyroad game with the turtle module as a python prgoram
#The program uses multiple python files to be able to run the game as one. the car_manaer, player and scoreboard


####CARMANAGER
#The CarManager class is designed to handle the creation and movement of cars in a game. It maintains a list of car
# objects, which are generated and managed by the class.

#create_cars class - The cars are created randomly, with a 1 in 6 chance of being added to the screen.
# Each car is initialized as a rectangular shape, with a random color chosen from a predefined set, and is positioned
# at a random y-coordinate along the right edge of the screen.

#The move method is responsible for moving all the cars from right to left across the screen. It simulates the cars
# driving across the screen at a constant speed.

#move_faster method that increases the speed of all the cars, making them move faster by adding an increment to their
# movement distance. This allows for dynamic gameplay, where the speed of the cars can increase over time or in response
# to certain game conditions.


######PLAYERCLASS
#The Player class models the player character in a game, specifically a turtle that the player controls.
# It inherits from the Turtle class and is initialized with a turtle shape, white color, and a starting position at the
# bottom center of the screen. The turtle is also oriented to face upwards, ready to move towards the top.

#The move method allows the player to move the turtle forward by a fixed distance, simulating the player advancing
# towards the finish line.

#The reset_position method is used to send the turtle back to its starting position, typically after reaching the finish line


####SCOREBOARD
#The Scoreboard class manages the display of the player's level and the game-over message in a game. Inheriting from
# the Turtle class, it is initialized with a hidden turtle cursor and is positioned at the top left of the screen.
# The scoreboard starts by displaying the initial level, set to 1, using a predefined font.

#The level_increase method is responsible for updating the level on the screen. Each time it is called,
# it clears the previous level display, increments the level by one, and writes the new level on the screen.

#The game_over method is used to display a "GAME OVER" message at the center of the screen when the game ends,
# signaling to the player that the game is over.