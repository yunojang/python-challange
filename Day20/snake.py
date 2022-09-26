from shutil import move
from this import d
import time
from turtle import Turtle, Screen


class Body(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        # self.shapesize(2)


SIZE = 20
# left down right up
DIRECTION = {
    "Up": 90,
    "Down": 270,
    "Left": 180,
    "Right": 0,
}
START_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.direction = "Right"
        self.speed = 0.8
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            body = Body()
            body.setpos(pos)
            self.segments.append(body)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            foraward = self.segments[i - 1]
            (new_x, new_y) = foraward.pos()
            self.segments[i].setpos(new_x, new_y)

        self.head.setheading(DIRECTION[self.direction])
        self.head.forward(SIZE)

    def set_dirction(self, direction: str):
        self.direction = direction

    def up(self):
        if self.direction != "Down":
            self.set_dirction("Up")
        # self.segments[0].setheading(DIRECTIONS[1])

    def down(self):
        if self.direction != "Up":
            self.set_dirction("Down")
        # self.segments[0].setheading(DIRECTIONS[3])

    def left(self):
        if self.direction != "Right":
            self.set_dirction("Left")
        # self.segments[0].setheading(DIRECTIONS[2])

    def right(self):
        if self.direction != "Left":
            self.set_dirction("Right")
        # self.segments[0].setheading(DIRECTIONS[0])
