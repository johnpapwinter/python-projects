from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        if self.xcor() > 320:
            return
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if self.xcor() < -320:
            return
        self.goto(new_x, self.ycor())

