from random import randint
from secrets import choice
from turtle import Turtle

COLORS = ["brown", "red", "purple", "blue", "green", "yellow", "skyblue"]


class Car(Turtle):
    def __init__(self, pos, direction, speed) -> None:
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.color(choice(COLORS))
        self.setpos(pos)
        self.move_speed = speed
        self.direction = direction

    def run_cross(self):
        next = self.move_speed * self.direction
        self.setx(self.xcor() + next)


start_x = [-320, 320]


class Car_Manager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = 2
        self.percent = 40

    def regen_car(self):
        random_chance = randint(0, self.percent) >= self.percent

        if not random_chance:
            return

        is_left = randint(0, 1) == 0

        pos_x = start_x[0] if is_left else start_x[1]
        pos_y = randint(-200, 200)
        pos = (pos_x, pos_y)
        direction = 1 if is_left else -1

        self.cars.append(Car(pos, direction, self.car_speed))

    def move_cars(self):
        for car in self.cars:
            car.run_cross()

    def create_cars(self, count):
        for _ in range(count):
            self.append_car()

    def level_up(self):
        self.car_speed += 1
        self.percent = int(self.percent * 0.8)
