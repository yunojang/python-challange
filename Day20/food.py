from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self, max_x, max_y) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("blue")
        self.shapesize(0.5)  # 10
        self.speed("fastest")

        self.max_x = max_x
        self.max_y = max_y

        self.pos_random()

    def pos_random(self):
        rand_x = randint(-self.max_x, self.max_x)
        rand_y = randint(-self.max_y, self.max_y)

        self.setpos(rand_x, rand_y)
