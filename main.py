import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
state_list = data.state.tolist()
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title = f"{len(guessed)}/50 States Correct",
                                    prompt = "What's another states name?").title()
    if answer_state == "End":
        missing_states = [state for state in state_list if state not in guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.state == answer_state]
        t.goto(int(answer_data.x), int(answer_data.y))
        t.write(answer_state)
