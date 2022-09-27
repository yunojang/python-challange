from random import choice, random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.random_dirction()

    def random_dirction(self):
        x_random = random() + 1.5
        y_random = random() + 1.5
        self.x_speed = choice([-x_random, x_random])
        self.y_speed = choice([-y_random, y_random])

    def speed_up(self):
        self.x_speed *= 1.1
        self.y_speed *= 1.1

    def move(self):
        next_x = self.xcor() + self.x_speed
        next_y = self.ycor() + self.y_speed
        self.setpos((next_x, next_y))

    def turn_y(self):
        self.y_speed *= -1

    def turn_x(self):
        self.x_speed *= -1
        self.speed_up()

    def reset_pos(self):
        self.setpos(0, 0)
        self.random_dirction()
