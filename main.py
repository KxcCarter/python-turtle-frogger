import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_SPEED = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
my_turt = Player()
garage = CarManager()

screen.listen()
screen.onkey(my_turt.go_turtle_go, 'Up')



game_is_on = True
while game_is_on:
    time.sleep(STARTING_SPEED)
    screen.update()
    garage.new_car()
    garage.drive_cars()

    for car in garage.all_cars:
        if my_turt.distance(car) <= 20:
            print('MY TURT IS HURT!')
            score.game_over()
            game_is_on = False

    if my_turt.ycor() >= 280:
        my_turt.back_to_start()
        score.add_point()
        STARTING_SPEED *= 0.9
        # garage.increase_speed()


screen.exitonclick()