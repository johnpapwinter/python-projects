from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

PLAYER_LIVES = 3

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen._root.resizable(False, False)
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

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(player_paddle) < 25:
        ball.bounce_y()

    if ball.ycor() < -300:
        PLAYER_LIVES -= 1
        ball.reset_pos()

    if PLAYER_LIVES <= 0:
        game_in_on = False
        print("GAME OVER")

screen.exitonclick()

# if __name__ == '__main__':
#     pass
