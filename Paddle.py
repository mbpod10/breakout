from turtle import Turtle

Y_BOUNDS = -200
X_BOUNDS = 500


RIGHT = 0
LEFT = 180


CONISTENT_FORWARD = 30


class Paddle (Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.setheading(RIGHT)
        self.goto(0, Y_BOUNDS)

    def left(self):
        self.setheading(LEFT)
        self.forward(CONISTENT_FORWARD)

    def right(self):
        self.setheading(RIGHT)
        self.forward(CONISTENT_FORWARD)

    def set_user_contraints(self):
        if self.xcor() >= X_BOUNDS:
            print("OUT OF BOUNDS~")
            self.goto(X_BOUNDS, Y_BOUNDS)
        if self.xcor() <= -X_BOUNDS:
            print("OUT OF BOUNDS~")
            self.goto(-X_BOUNDS, Y_BOUNDS)
