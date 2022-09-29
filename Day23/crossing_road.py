from time import sleep
from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

max_x = screen.window_width() / 2
max_y = screen.window_height() / 2

# score
score = Scoreboard((-max_x + 50, max_y - 20))

# player
player = Player((0, -max_y + 30))

screen.onkey(fun=player.go_up, key="Up")
screen.onkey(fun=player.go_down, key="Down")
# screen.onkey(fun=player.go_left, key="Left")
# screen.onkey(fun=player.go_right, key="Right")

# car
car_manage = Car_Manager()

game_is_on = True
level = 1
while game_is_on:
    sleep(0.001)

    car_manage.regen_car()
    car_manage.move_cars()
    screen.update()

    # colision next level
    if player.ycor() >= max_y:
        level += 1
        if level == 11:
            score.win()
            game_is_on = False
        score.increase_level()
        player.reset_pos()
        car_manage.level_up()

    # colision car
    for car in car_manage.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
