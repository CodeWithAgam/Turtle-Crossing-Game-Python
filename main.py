# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Scoreboard

# Setting up the Screen
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

# Setting up the Player, Cars and Scoreboard
player = Player()
car = Cars()
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
    car.create_car()
    car.move()

    # Detect collision with the Car
    for car in car.cars_list:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Detect if the Player has reached the finish line
    if player.ycor() > 280:
        player.start()
        car.level_up()
        scoreboard.update()

s.exitonclick()