from turtle import Turtle

class Ball(Turtle):

    def __init__(self, m_s_i: bool = False) -> None:
        super().__init__()

        # setting up object to look like ball
        self.penup()
        self.shape("circle")
        self.color("white")

        # setting up attributes 
        self.x_move = 10        # units to move in one move in x axis
        self.y_move = 10        # units to move in one move in y axis
        self.move_speed = 0.1   # frequency of updating screen - time.sleep() value between screen updates
        self.move_speed_increase = m_s_i    # allows player to play on hard mode which means move_speed is increased by decreasing sleep time between screen updates
    
    def move(self):
        """Method makes ball move. Direction is dependant on current values of x_move and y_move attributes."""

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """Method makes ball bounce in y axis by changing changing y_move attribute value by multiplying it by -1."""

        self.y_move *= -1
    
    def bounce_x(self):
        """Method makes ball bounce in x axis by changing changing x_move attribute value by multiplying it by -1."""

        self.x_move *= -1

        # if increasing is active move_speed attribute value will be decreased every time bounce_x is activated - ball bounces off paddle
        if self.move_speed_increase is True:
            self.move_speed *= 0.9


    def refresh(self):
        """Method sets ball up in middle of map and changes its x axis direction."""
        self.goto(x = 0, y = 0)
        self.bounce_x()

        # if increasing is active move_speed attribute move_speed value is set to 0.1 as it was changes in round before, and new round should start with its value equal 0.1
        if self.move_speed_increase is True:
            self.move_speed = 0.1