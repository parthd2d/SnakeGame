from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.color("purple")
        self.pensize(width=5)
        self.penup()
        self.setposition(-295,-285)
        self.pendown()

    def bottom_boundary(self):
        self.penup()
        self.goto(-300,-293)
        self.pendown()
        self.setheading(0)
        self.forward(592)

    def right_boundary(self):
        self.penup()
        self.goto(292,-293)
        self.pendown()
        self.setheading(90)
        self.forward(590)

    def top_boundary(self):
        self.penup()
        self.goto(292,300)
        self.pendown()
        self.setheading(180)
        self.forward(590)

    def left_boundary(self):
        self.penup()
        self.goto(-300,300)
        self.pendown()
        self.setheading(270)
        self.forward(590)

    def make_boundary(self):
        self.bottom_boundary()
        self.right_boundary()
        self.top_boundary()
        self.left_boundary()
        self.penup()
        self.goto(-300,243)
        self.pendown()
        self.setheading(0)
        self.forward(590)