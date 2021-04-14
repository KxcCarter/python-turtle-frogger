from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.write(f"You have {self.points} points!", align="left", font=FONT)

    def add_point(self):
        self.clear()
        self.points += 1
        self.update_score()

    def reset_score(self):
        self.clear()
        self.points = 0
        self.update_score()