from turtle import Turtle

GRID_UNIT = 20
WID = 5
LEN = 1


class Paddle(Turtle):
    def __init__(self, pos) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.turtlesize(stretch_wid=WID, stretch_len=LEN)
        self.setpos(pos)

    def go_up(self):
        self.sety(self.ycor() + GRID_UNIT)

    def go_down(self):
        self.sety(self.ycor() - GRID_UNIT)
