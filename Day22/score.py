from turtle import Turtle

AIIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self, max_y):
        super().__init__()
        self.score = [0, 0]
        self.pu()
        self.ht()
        self.color("white")

        self.setpos(0, max_y - 50)
        self.draw_score()

    def draw_score(self):
        self.clear()

        self.setx(-65)
        left_score = self.score[0]
        self.write(str(left_score), align=AIIGNMENT, font=FONT)

        self.setx(+65)
        right_score = self.score[1]
        self.write(str(right_score), align=AIIGNMENT, font=FONT)

    def score_increase(self, index):
        self.score[index] += 1
        self.draw_score()

    def score_left(self):
        self.score_increase(0)

    def score_right(self):
        self.score_increase(1)
