from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.speed(0)
        self.start()

    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
