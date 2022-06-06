from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write("Level: {}".format(self.level), align="left", font=FONT)
        self.score = 0

    def update(self):
        self.clear()
        self.level += 1
        self.write("Level: {}".format(self.level), align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)