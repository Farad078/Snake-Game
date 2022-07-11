from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def move_up():
    snake.move_up()


def move_down():
    snake.move_down()


def move_left():
    snake.move_left()


def move_right():
    snake.move_right()


screen = Screen()
# user = screen.textinput(title="Game Level", prompt="Please enter your level (slow or slowest or fast or fastest):")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count()

    if (snake.head.xcor() > 280) or (snake.head.xcor() < -300) or (snake.head.ycor() > 300) or (snake.head.ycor() < -280):
        score.reset()
        snake.refresh()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.refresh()










screen.exitonclick()