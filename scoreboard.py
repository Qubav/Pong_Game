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

        # showing scoreboard
        self.update_scoreboard()


    def l_point(self):
        """Function increases l_score attribute value by 1 and refreshes scoreboard."""

        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        """Function increases r_score attribute value by 1 and refreshes scoreboard."""
        
        self.r_score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Function clears old scoreboard and writes updated."""

        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align = "center", font = ("Courier", 60, "normal"))