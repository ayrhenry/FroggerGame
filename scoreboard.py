from turtle import Turtle 
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-230, 260)
        self.write((f"Level: {self.level}"), align="center", font=("Courier", 15, "normal"))

    def update_level(self):
        self.clear() 
        self.goto(-230, 260)
        self.level += 1
        self.write((f"Level: {self.level}"), align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write((f"Game Over"), align="center", font=("Courier", 60, "normal"))