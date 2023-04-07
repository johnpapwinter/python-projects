from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, left_wall, right_wall):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color("white")
        self.penup()
        self.goto(position)
        self.left_wall = left_wall
        self.right_wall = right_wall

    def go_right(self):
        new_x = self.xcor() + 20
        if self.xcor() > self.right_wall:
            return
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if self.xcor() < self.left_wall:
            return
        self.goto(new_x, self.ycor())

