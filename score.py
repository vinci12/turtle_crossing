from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('pink')
        self.penup()
        self.hideturtle()
        self.goto(250, 260)
        self.score = 0

    def update_score(self):
        """Clear the old score and write the new one on screen."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
    
    def increase_score(self):
        """Increase score and refresh display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Display Game Over message in the middle of the screen."""
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        