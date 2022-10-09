import pandas
import turtle
from turtle import Screen, Turtle, circle

screen = Screen()
image_path = "blank_states.gif"
screen.addshape(image_path)

turtle.shape(image_path)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
missing_states = states
guessed_states = []

def draw_state(state, x, y):
    writer = Turtle()
    writer.pu()
    writer.shape("circle")
    writer.turtlesize(0.1)
    writer.setpos(x, y)
    writer.write(state)


while len(states) > 0:
    user_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(states)} Guess State", prompt="Input another state"
    )

    user_state = user_state.title() # title is upper to first char

    if user_state == "Exit":
        missing_states = [state for state in missing_states if state not in guessed_states]
        break

    if user_state in missing_states:
        guessed_states.append(user_state)

        correct = data[data.state == user_state]
        draw_state(user_state, int(correct.x), int(correct.y))

# screen.mainloop()
# rest states csv
pandas.Series(missing_states).to_csv("states_to_learn.csv")
