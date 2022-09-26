from turtle import Turtle, Screen
import heroes

print(heroes.gen())

t = Turtle()
t.shape("turtle")
t.color("tomato")


def draw_rect(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)


draw_rect(100)
draw_rect(200)
draw_rect(300)
draw_rect(400)


screen = Screen()
screen.exitonclick()
