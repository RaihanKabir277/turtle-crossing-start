
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.score = 0
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level = {self.level}", align="center",font=FONT)
        self.goto(200,260)
        self.write(f"Score = {self.score}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()
    
    def score_up(self):
        self.score += 5
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
    
