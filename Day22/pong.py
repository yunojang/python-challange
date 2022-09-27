from time import sleep
from turtle import Screen, Turtle
from score import Scoreboard
from ball import Ball
from paddle import Paddle

WIDTH = 800
HEIGHT = 600

max_x = WIDTH / 2
max_y = HEIGHT / 2

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()

# bg
FONT = ("Courier", 12, "normal")

bg = Turtle()
bg.color("white")
bg.ht()
bg.write("Pong Game", align="center", font=FONT)

# paddle
PAD = 50
paddle_pos = max_x - PAD
paddle_right = Paddle((paddle_pos, 0))
paddle_left = Paddle((-paddle_pos, 0))

screen.onkeypress(key="Up", fun=paddle_right.go_up)
screen.onkeypress(key="Down", fun=paddle_right.go_down)
screen.onkeypress(key="w", fun=paddle_left.go_up)
screen.onkeypress(key="s", fun=paddle_left.go_down)

# ball
ball = Ball()
ball_size = ball.shapesize()[0] * 20

# scoreboard
score = Scoreboard(max_y)

game_is_on = True
while game_is_on:
    sleep(0.001)
    screen.update()
    ball.move()

    # collistion top or bottom
    collision_top = ball.ycor() + ball_size / 2 >= max_y
    collision_bottom = ball.ycor() - ball_size / 2 <= -max_y

    if collision_top or collision_bottom:
        ball.turn_y()

    # collistion paddle
    left_distance = abs((ball.xcor() - 10) - (-paddle_pos + 10))
    collision_paddle_left = (
        left_distance < abs(ball.x_speed) and ball.distance(paddle_left) <= 50
    )

    right_distance = abs((ball.xcor() + 10) - (paddle_pos - 10))
    collision_paddle_right = (
        right_distance < abs(ball.x_speed) and ball.distance(paddle_right) <= 50
    )

    if collision_paddle_left or collision_paddle_right:
        ball.turn_x()

    # paddle missed
    # missed right
    if ball.xcor() + 10 > max_x:
        ball.reset_pos()
        score.score_left()
    # missed left
    elif ball.xcor() - 10 < -max_x:
        ball.reset_pos()
        score.score_right()

screen.exitonclick()
