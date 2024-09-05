from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, align="center", font=("Comic Sans MS",
                                                                                                        20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_refresh()
