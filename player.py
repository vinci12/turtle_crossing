START_POS = (0,-270)
FINISH_LINE = 280
MOVENT_PLAYER = 10


from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(START_POS)

    def move_up(self):
        y_new = self.ycor()+MOVENT_PLAYER
        self.goto(0,y_new)

    def reset(self):
            self.goto(START_POS)
    
    def reached_finish(self):
        """Check if player has crossed the finish line."""
        return self.ycor() > FINISH_LINE

    