from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self, top_pos):
        super().__init__()
        self.level = 1
        self.pu()
        self.ht()
        self.setpos(top_pos)

        self.draw_level()

    def increase_level(self):
        self.level += 1
        self.draw_level()

    def draw(self, arg):
        self.write(arg, align=ALINGMENT, font=FONT)

    def draw_level(self):
        self.clear()
        self.draw(f"Level {self.level}")

    def game_over(self):
        self.setpos(0, 0)
        self.draw(f"GAME OVER")

    def win(self):
        self.setpos(0,0)
        self.draw(f"YOU WIN")