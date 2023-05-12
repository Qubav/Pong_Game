from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position: tuple) -> None:
        super().__init__()

        # setting up paddle appearance
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()

        # setting up paddle position
        self.goto(position)

    def go_up(self):
        """Method moves paddle 20 units to top."""

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Method moves paddle 20 units to bottom."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
