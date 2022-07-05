from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

class State(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.data = pandas.read_csv("50_states.csv")
        self.states_list = self.data["state"].to_list()
        self.x_list = self.data["x"].to_list()
        self.y_list = self.data["y"].to_list()

    def state_name(self):
        return self.states_list

    def state_x(self, i):
        return self.x_list[i]

    def state_y(self, i):
        return self.y_list[i]

    def print_state(self, player_input):
        i = self.states_list.index(f"{player_input}")
        x = self.state_x(i)
        y = self.state_y(i)
        self.goto(x, y)
        self.write(f"{player_input}", False, align=ALIGNMENT, font=FONT)

# state = State()
# print(state.states_list)
# print(state.states_list.index("Texas"))
# print(state.x_list[state.states_list.index("Texas")])
# print(state.y_list[state.states_list.index("Texas")])
