from turtle import Turtle

TEXT_HEIGHT = 255

ALIGNMENT = "center"
FONT = ('Courier', 19, 'normal')
GAME_OVER_FONT = ('Courier', 50, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, TEXT_HEIGHT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", False, ALIGNMENT, GAME_OVER_FONT)
