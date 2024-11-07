from turtle import *

class Paddle(Turtle):

#setting up paddle on the right
    def __init__ (self, position):
        super().__init__()   
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1) #paddle size
        self.penup()
        self.goto(position)

#moving the paddle
    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)