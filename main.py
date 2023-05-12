from game import Game

if __name__ == "__main__":
    game = Game()
    game.play()

# from turtle import Screen
# from paddle import Paddle
# from ball import Ball
# import time
# from scoreboard import Scoreboard

# L_PADDLE_POS = (-350, 0)
# R_PADDLE_POS = (350, 0)

# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong")
# screen.tracer(0)

# scoreboard = Scoreboard()

# r_paddle = Paddle(R_PADDLE_POS)
# l_paddle = Paddle(L_PADDLE_POS)
# ball = Ball(True)

# game_is_on = True

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
    
#     # detection collision

#     if ball.ycor() >= 280 or ball.ycor() <= -280:
#         ball.bounce_y()

#     # detect collision with right paddle

#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()

#     # detect if ball missed a paddle
#     if ball.xcor() < -360:
#         ball.refresh()
#         scoreboard.r_point()

#     if ball.xcor() > 360:
#         ball.refresh()
#         scoreboard.l_point()

# screen.exitonclick()