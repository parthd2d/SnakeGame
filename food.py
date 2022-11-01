from turtle import Turtle
from random import randint

# Done

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.hideturtle()
        self.goto(x=randint(-265, 265), y=randint(-260, 225))
        self.showturtle()
