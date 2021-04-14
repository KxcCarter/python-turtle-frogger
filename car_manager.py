from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.new_car()

    def drive_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, random.randrange(-250, 250, 30))
            self.all_cars.append(car)

    def increase_speed(self):
        """
        Increases the speed of the cars, but does not effect the frequency of dispatch.
        :return:
        """
        self.car_speed += MOVE_INCREMENT
