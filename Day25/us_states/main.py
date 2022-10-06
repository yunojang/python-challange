import turtle
from turtle import Screen, Turtle

import pandas
from pandas import DataFrame

screen = Screen()

screen.title("U.S States Game")
image_path = "blank_states.gif"
screen.addshape(image_path)

turtle.shape(image_path)


# def on_click(x, y):
#     print(x, y)


# screen.onclick(on_click)
score = 0
states_data = pandas.read_csv("50_states.csv")
writer = Turtle()


def draw_state(state, x, y):
    writer.pu()
    writer.ht()
    writer.setpos(x, y)
    writer.write(state)


game_continue = True

while game_continue:
    user_input = screen.textinput(
        title=f"{score}/{len(states_data)} Guess state", prompt="Input another state name"
    )

    if user_input == None:
        game_continue = False

    # correspond = states[states.state == user_input]
    # print(Series.to_list(correspond))
    correct_state = ''

    for state in states_data.state:
        if state.lower() == user_input.lower():
            correct_state = state

    correct_state_data = states_data[states_data.state == correct_state]
    if correct_state:
        s, x, y = list(correct_state_data.state)[0], list(correct_state_data.x)[0], list(correct_state_data.y)[0]
        draw_state(s,x,y)
        score += 1 


screen.mainloop()
# screen.exitonclick()``
