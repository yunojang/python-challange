from turtle import Screen, Turtle
from functools import partial

t = Turtle()
screen = Screen()

screen.listen()


def move_forward(dist):
    t.forward(dist)


def move_backword(dist):
    t.backward(dist)


def rotate(angle):
    t.setheading(t.heading() + angle)


speed = 10

screen.onkey(fun=partial(move_forward, speed), key="w")
screen.onkey(fun=partial(move_backword, speed), key="s")
screen.onkey(fun=partial(rotate, +10), key="a")
screen.onkey(fun=partial(rotate, -10), key="d")
screen.onkey(fun=screen.resetscreen, key="c")


screen.exitonclick()
