from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align='Center', font=('Arial', 14, 'normal'))

    def count(self):
        self.score += 1
        self.update()

    def game_status(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game is Over!!", align='Center', font=('Arial', 14, 'normal'))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.score = 0
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))
            self.update()
        else:
            self.score = 0
            self.update()

    def score(self):
        self.score = 0



