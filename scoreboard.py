from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()

        # setting up scoreboard appearance
        self.color("white")
        self.hideturtle()
        self.penup()

        # setting up attributes values 
        self.l_score = 0
        self.r_score = 0
        
        # drawing vertical dashed line in middle of screen
        self.mid_line: list [Turtle] = []
        self.middle_line()

        # showing scoreboard
        self.update_scoreboard()


    def l_point(self):
        """Method increases l_score attribute value by 1 and refreshes scoreboard."""

        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        """Method increases r_score attribute value by 1 and refreshes scoreboard."""
        
        self.r_score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Method clears old scoreboard and writes updated."""

        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align = "center", font = ("Courier", 60, "normal"))
    
    def middle_line(self):
        """Method draws vertical dashed line in middle of the screen."""

        for i in range(15):

            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.shapesize(stretch_wid = 0.5, stretch_len = 0.2)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x = 0, y = -280 + i * 40)