from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day 024/snake-game-part-3/highest_score.txt") as data:
            self.highest_score = int(data.read())    
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()
 
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("Day 024/snake-game-part-3/highest_score.txt", "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
 

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
