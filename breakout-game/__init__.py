from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT GAME")
screen.tracer(0)

player_paddle = Paddle((0, -280))
ball = Ball()

screen.listen()
screen.onkeypress(player_paddle.go_left, "Left")
screen.onkeypress(player_paddle.go_right, "Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(player_paddle) < 25:
        ball.bounce_y()


screen.exitonclick()

# if __name__ == '__main__':
#     pass
