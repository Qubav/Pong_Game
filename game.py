from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

L_PADDLE_POS = (-350, 0)
R_PADDLE_POS = (350, 0)

class Game:

    def __init__(self, hard_mode: bool = False) -> None:
        
        # setting up Screen class object that will be game screen
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

        # setting up objects from classes Scoreboard, Paddle and Ball that will be used to perform game
        self.scoreboard = Scoreboard()
        self.r_paddle = Paddle(R_PADDLE_POS)
        self.l_paddle = Paddle(L_PADDLE_POS)
        self.ball = Ball(hard_mode)
        
        # setting up attribute which value determines if game lasts
        self.game_is_on = True

    def end_game(self):
        """Function sets game_is_on attribute value to False. Games stops and player can click to make screen to disappear."""

        self.game_is_on = False

    def play(self):

        # setting up screen attribute to interact with keyboard keys
        self.screen.listen()
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")
        self.screen.onkey(self.end_game, "o")

        # main loop
        while self.game_is_on:
            
            # time for objects to move
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()
            
            # collision with top and bottom walls detection and bounce_y method activation
            if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
                self.ball.bounce_y()

            # collision with paddle detecting and bounce_x method activating
            if self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320 or self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()

            # detecting if ball went trough left paddle, refreshing all position and giving point for player from right side
            if self.ball.xcor() < -360:
                self.ball.refresh()
                self.scoreboard.r_point()

            # detecting if ball went trough right paddle, refreshing all position and giving point for player from left side
            if self.ball.xcor() > 360:
                self.ball.refresh()
                self.scoreboard.l_point()

        self.screen.exitonclick()


