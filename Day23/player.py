from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self, start_pos) -> None:
        super().__init__()
        self.start_pos = start_pos
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.color()
        self.left(90)

        self.reset_pos()

    def go_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def go_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def go_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def reset_pos(self):
        self.setpos(self.start_pos)
