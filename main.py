import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turt = Player()

screen.listen()
screen.onkey(my_turt.go_turtle_go, 'Up')

all_cars = []

for each in range(1, 15):
    broom_broom = CarManager()
    all_cars.append(broom_broom)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in all_cars:
        car.drive()

screen.exitonclick()