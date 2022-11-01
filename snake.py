from turtle import Turtle

STARTING_SIZE = 3
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.size = STARTING_SIZE
        self.initialize_segments()
        self.head = self.segments[0]

    def initialize_segments(self):
        x_cor = (STARTING_SIZE * 20) -5
        for i in range(STARTING_SIZE):
            self.add_segment((x_cor, 5))
            x_cor -= 20

    def add_segment(self, pos):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        pos = self.segments[-1].position()
        self.add_segment(pos)
        self.size += 1

    def move(self):
        for i in range(self.size - 1, 0, -1):
            pos = self.segments[i - 1].position()
            self.segments[i].goto(pos)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.head.forward(MOVE_DISTANCE)
