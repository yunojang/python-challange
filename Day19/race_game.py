from random import random, randint
from turtle import Turtle, Screen, speed, textinput

screen_width = 600
screen_height = 400
padding = 50
end_line = screen_width / 2 - padding
start_line = -end_line


def draw_end_line():
    pen = Turtle()
    pen.pensize(10)
    pen.pu()
    pen.setpos(end_line, screen_height / 2)
    pen.pd()
    pen.right(90)
    pen.forward(screen_height)


screen = Screen()
screen.setup(width=screen_width, height=screen_height)


class Race_Turtle(Turtle):
    def __init__(self, color, pos) -> None:
        super().__init__(shape="turtle")
        self.speed = 1
        self.color(color)
        self.move(pos)
        self.max_speed = randint(10, 35)
        self.race_fin = False

    @staticmethod
    def random_speed(max_speed):
        return random() * max_speed

    def move(self, pos):
        self.pu()
        self.setpos(pos)
        self.pd()

    def step(self) -> None:
        self.move_speed = Race_Turtle.random_speed(self.max_speed)
        self.forward(self.move_speed)

        if self.xcor() >= end_line:
            self.race_fin = True

    def describe(self):
        print(f"{self.pencolor()}'s status")
        print(f"max_speed: {self.max_speed}")


turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []

draw_end_line()

for i in range(len(turtle_colors)):
    color = turtle_colors[i]
    turtle = Race_Turtle(
        color=color, pos=(start_line, screen_height / 2 - padding * (i + 1))
    )
    racers.append(turtle)

user_bet = screen.textinput(
    "Select your turtle",
    f"Which turtle will win the race? \n Enter a color: {turtle_colors}",
)

is_race_on = True
winner = ""

while is_race_on:
    for racer in racers:
        racer.step()

        if racer.race_fin:
            is_race_on = False
            winner = racer.pencolor()

print(
    f"You {'Win' if user_bet == winner else 'Lose'}, Winner is {winner} (Your pick: {user_bet})"
)

for racer in racers:
    racer.describe()
