from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):  
        random_chance = random.randint(1, 6)
        if random_chance == 1: 
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            # random_x = random.randint()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_increment(self):
        self.car_speed += MOVE_INCREMENT

