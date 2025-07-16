import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("CROSS RACING GAME")
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #random cars generator
    cars.create_cars()
    cars.car_move()

    #detect the colision with cars here

    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False



    #detect the finish line
    if player.win():
        player.goto_start()
        cars.speed_increment()
    else:
        game_is_on = False
    
     


screen.exitonclick()
