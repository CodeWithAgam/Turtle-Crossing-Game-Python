# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import time
from turtle import Screen
from player import Player
from assets import Car
from score import Scoreboard

# Setting up the Screen
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

# Setting up the Player, Cars and Scoreboard
player = Player()
car = Car()
scoreboard = Scoreboard()

# Setting up the Controls
s.listen()
s.onkeypress(player.move, "Up")
s.onkeypress(player.move, "w")

game_on = True
while game_on:
    time.sleep(0.1)
    s.update()

    # Create the Cars
    car.create()
    car.move()

    # Detect collision with the Car
    for car in car.cars_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    # Detect if the Player has reached the finish line
    if player.ycor() > 280:
        player.change_level()
        # scoreboard.update_score()

s.exitonclick()