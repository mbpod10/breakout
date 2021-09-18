import time
from turtle import Turtle, Screen
from Paddle import Paddle


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

paddle = Paddle()
game_on = True


screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
