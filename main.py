from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from margins import Boundary

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score_board = ScoreBoard()
my_boundary = Boundary()
my_boundary.make_boundary()
game_is_on = True
screen.listen()

screen.onkey(key="s", fun=my_snake.down)
screen.onkey(key="w", fun=my_snake.up)
screen.onkey(key="a", fun=my_snake.left)
screen.onkey(key="d", fun=my_snake.right)

while game_is_on:

    my_snake.move()
    screen.update()
    time.sleep(0.1)

    if my_snake.head.distance(x=my_food) < 20:
        my_food.refresh()
        my_score_board.increment_score()
        my_snake.extend()

    if my_snake.head.xcor() > 285 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 240 or my_snake.head.ycor() < -280:
        game_is_on = False
        my_score_board.game_over()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_score_board.game_over()

screen.exitonclick()
