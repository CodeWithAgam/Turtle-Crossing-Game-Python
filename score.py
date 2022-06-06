from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.score_text = self.write("Score: {}".format(self.score), align="center", font=FONT)
