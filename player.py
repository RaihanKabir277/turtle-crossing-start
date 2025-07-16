
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super(). __init__()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto_start()
    
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)
    
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0,new_y)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
