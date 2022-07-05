from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.write("Time's up! GAME OVER.", False, align=ALIGNMENT, font=FONT)

    def game_won(self):
        self.write("You Won!", False, align=ALIGNMENT, font=FONT)