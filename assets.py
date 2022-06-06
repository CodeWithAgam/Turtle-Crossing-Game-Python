from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE = 10


class Car():
    def __init__(self):
        super().__init__()
        self.cars_list = []

    def create(self):
        random_num = randint(1, 6)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            car.setheading(180)
            car.goto(300, randint(-250, 250))
            self.cars_list.append(car)

    def move(self):
        for car in self.cars_list:
            car.forward(STARTING_DISTANCE)

