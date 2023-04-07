from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

PLAYER_LIVES = 3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEFT_WALL = (-SCREEN_WIDTH / 2) + 20
RIGHT_WALL = (SCREEN_WIDTH / 2) - 20
CEILING = (SCREEN_HEIGHT / 2) - 20
BOTTOM = -SCREEN_HEIGHT / 2
PADDLE_POSITION = (0, BOTTOM + 20)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen._root.resizable(False, False)
screen.title("BREAKOUT GAME")
screen.tracer(0)

player_paddle = Paddle(PADDLE_POSITION, LEFT_WALL, RIGHT_WALL)
ball = Ball()

screen.listen()
screen.onkeypress(player_paddle.go_left, "Left")
screen.onkeypress(player_paddle.go_right, "Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.xcor() > RIGHT_WALL or ball.xcor() < LEFT_WALL:
        ball.bounce_x()

    if ball.ycor() > CEILING:
        ball.bounce_y()

    if ball.distance(player_paddle) < 25:
        ball.bounce_y()

    if ball.ycor() < BOTTOM:
        PLAYER_LIVES -= 1
        ball.reset_pos()

    if PLAYER_LIVES <= 0:
        game_in_on = False
        print("GAME OVER")

screen.exitonclick()

# if __name__ == '__main__':
#     pass
