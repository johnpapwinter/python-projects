from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT")
screen.tracer(0)

player_paddle = Paddle((0, -280))

screen.listen()
screen.onkeypress(player_paddle.go_left, "Left")
screen.onkeypress(player_paddle.go_right, "Right")

game_in_on = True
while game_in_on:
    screen.update()


screen.exitonclick()

# if __name__ == '__main__':
#     pass
