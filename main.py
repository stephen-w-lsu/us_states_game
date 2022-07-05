from turtle import Screen
from states import State
from counter import Counter
from game_over import GameOver

screen = Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
state = State()
counter = Counter()
game_over = GameOver()
game_on = True

while game_on:

    first_input = screen.textinput("State Game", "What's a state name? ").title()

    if first_input in state.states_list:
        state.print_state(first_input)
        counter.add_one()
        after_first = True

    if first_input.lower() == "exit":
        after_first = False
        game_on = False

        while after_first:
            player_input = screen.textinput(f"{counter.total_guessed}/50 States Correct",
                                            "What's another state name? ").title()

            if player_input in state.states_list:
                state.print_state(player_input)
                counter.add_one()

            if player_input.lower() == "exit":
                after_first = False
                game_on = False

    if counter.total_guessed == 50:
        game_over.game_won()
        after_first = False
        game_on = False

