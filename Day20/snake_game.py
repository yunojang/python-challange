from time import sleep
from turtle import Turtle, Screen, update
from snake import Body, Snake
from food import Food
from scoreboard import Scoreborad

# screen
screen = Screen()
# remove turtel animation
screen.tracer(0)
screen.listen()

GRID_PIXEL_SIZE = 20
end_size = 600
screen.setup(width=end_size, height=end_size)
screen.bgcolor("black")

# scoreboard
score = Scoreborad(screen.window_height() / 2 - GRID_PIXEL_SIZE)

# snake
snake = Snake()
screen.update()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# food
max_x = screen.window_width() / 2 - GRID_PIXEL_SIZE
max_y = screen.window_height() / 2 - GRID_PIXEL_SIZE

food = Food(max_x, max_y)

game_is_on = True

while game_is_on:
    sleep(0.1)
    snake.move()  # all move
    screen.update()  # update

    # detect collision with food
    if snake.head.distance(food) <= 15:
        food.pos_random()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if (
        snake.head.xcor() > max_x
        or snake.head.xcor() < -max_x
        or snake.head.ycor() > max_y
        or snake.head.ycor() < -max_y
    ):
        game_is_on = False
        score.game_over()

    # detected collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) == 0:
            game_is_on = False
            score.game_over()


screen.exitonclick()
