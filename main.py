from turtle import *
from paddle import *
from ball import *
import time
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) #when the game starts the paddle starts from the center then goes right, to avoid this we use tracer and then update in the while loop when game is on later.

# Paddle class being inherited
left_paddle = Paddle((-350,0))
right_paddle = Paddle ((350,0))

# listening to keystrokes
screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down, "s")

#creating ball
ball = Ball()
#creating scoreboard
scoreboard = Scoreboard()


game_on = True
while game_on:
    time.sleep(ball.move_speed) #controlling the ball speed, lower the number, the faster
    screen.update() #reason to use is explained in step 6
    ball.move()

    #detect ball collision with top or bottom wall    
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    #detect collision with right paddle and left paddle
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    #detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()