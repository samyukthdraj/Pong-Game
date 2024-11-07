from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1 #this basically reverses the ball's direction so if the ball is in -280 it'll go to 280, if it's in 280, it'll go to -280
    def bounce_x(self):
        self.x_move *= -1 #same as bounce y but for x direction
        self.move_speed *=0.9
        
    def reset(self):
        self.goto(0,0) #ball resets 
        self.move_speed = 0.1
        self.bounce_x() # ball goes to the opposite direction from the start
