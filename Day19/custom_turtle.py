from turtle import Turtle


class Turtle:
    def __init__(self) -> None:
        self.turtle = Turtle()
        self.speed = 10

    def forward(self):
        self.turtle.forward(self.speed)

    def backward(self):
        self.turtle.backward(self.speed)
