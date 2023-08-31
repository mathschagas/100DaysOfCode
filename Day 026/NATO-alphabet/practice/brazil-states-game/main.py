import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil States Game")
image = "Day 026/practice/brazil-states-game/Brazil_Political_Map.gif"
screen.addshape(image)
turtle.shape(image)

states_df = pandas.read_csv("Day 026/practice/brazil-states-game/26_states.csv")
all_states = states_df["state"].to_list()
for state_i in range(len(all_states)):
    all_states[state_i] = all_states[state_i].title()
guessed_states = []


while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 States Correct",
                                    prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day 026/practice/brazil-states-game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_df[states_df["state"] == answer_state]
        t.goto(int(state_data['x'].iloc[0]), int(state_data['y'].iloc[0]))
        t.write(answer_state, align="center")

    
