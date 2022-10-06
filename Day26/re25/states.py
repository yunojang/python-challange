import pandas
from turtle import Screen, Turtle, circle

screen = Screen()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
score = 0


def draw_state(state, x, y):
    writer = Turtle()
    writer.pu()
    writer.shape("circle")
    writer.turtlesize(0.1)
    writer.setpos(x, y)
    writer.write(state)


while len(states) > 0:
    user_state = screen.textinput(
        title=f"{score}/{len(states)} Guess State", prompt="Input another state"
    )
    user_state = user_state.title()

    if user_state == "Exit":
        break

    if user_state in states:
        idx = states.index(user_state)
        states = states[0:idx] + states[idx + 1 :]

        correct = data[data.state == user_state]

        draw_state(user_state, int(correct.x), int(correct.y))
        score += 1

# screen.mainloop()
# rest states csv
pandas.Series(states).to_csv("states_to_learn.csv")
