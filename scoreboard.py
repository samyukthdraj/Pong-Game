from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear() #clears the score so that the current score doesnt get overlapped w the previous score
        self.goto(-100,185)
        self.write(self.left_score,align="center", font=("Courier", 70, "normal"))
        self.goto(100,185)
        self.write(self.right_score,align="center", font=("Courier", 70, "normal"))    

    def l_point(self):
        self.left_score += 1  
        self.update_score()  
    
    def r_point(self):
        self.right_score += 1  
        self.update_score()  
    