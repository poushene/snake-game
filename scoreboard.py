from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.clear()
        self.penup()
        self.sety(270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"S C O R E  :  {self.score}", False, align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E   O V E R", False, align=ALINGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

