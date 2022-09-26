from time import sleep
from turtle import Turtle, Screen, update
from snake import Body, Snake

screen = Screen()
# remove turtel animation
screen.tracer(0)
screen.listen()

end_size = 600
screen.setup(width=end_size, height=end_size)
screen.bgcolor("black")

snake = Snake()
screen.update()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    sleep(1 - snake.speed)
    snake.move()  # all move
    screen.update()  # update


screen.exitonclick()
