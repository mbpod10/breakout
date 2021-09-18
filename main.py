import time
from turtle import Turtle, Screen
from Paddle import Paddle
from Target import Target


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

paddle = Paddle()
game_on = True

for x in range(-450, 500, 50):
    target = Target(x, 250, 'red')
    target = Target(x, 220, 'orange')
    target = Target(x, 190, 'yellow')
    target = Target(x, 160, 'green')


screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    paddle.set_user_contraints()


screen.exitonclick()
