from this import d
from turtle import Turtle

AIIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreborad(Turtle):
    def __init__(self, height) -> None:
        super().__init__()
        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.pu()
        self.setpos(0, height)
        self.draw_score()
        self.ht()

    def draw_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=AIIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.draw_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=AIIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.high_score, self.score)
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

        self.score = 0
        self.draw_score()
