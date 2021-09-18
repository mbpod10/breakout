from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green"]

y_axes = []

for x in range(-500, 500, 50):
    y_axes.append(x)


class Target (Turtle):

    def __init__(self, x_corrdinate, const_y_corrd, _color):
        super().__init__()
        self.y_axes = y_axes
        self.shape('square')
        self.penup()
        self.color(_color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)

        self.goto(x_corrdinate, const_y_corrd)
        # self.goto(random.randint(-280, 300), random.choice(y_axes))
        # self.position()
