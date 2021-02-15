# File Name: carbajal_joshua_AS09.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS09.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS09.py

# Joshua Carbajal
# Date (10/24/19)
# AS.09
# Three Ball Bounce
# Purpose: Simulate three balls bouncing in along a line. The balls bounce off 
#          each other and the two walls on the edges.  When the balls contact 
#          each other they just change directions and travel at the same speed.  

from graphics import *
import random
import math

WIN_SIZE = 600
UPDATE_RATE = 30
xDir1 = 1
xDir2 = 0.5
xDir3 = -1.5
RADIUS = 20

# Creates graphics window
win = GraphWin("3 Ball Bounce", WIN_SIZE, WIN_SIZE)

# Creates three individual circles on graphics window 
ball_1 = Circle(Point(100,300), RADIUS)
ball_1.setFill("DarkRed")
ball_1.setOutline("Black")
ball_1.setWidth(3)
ball_1.draw(win)

ball_2 = Circle(Point(300,300), RADIUS)
ball_2.setFill("LightGreen")
ball_2.setOutline("Black")
ball_2.setWidth(3)
ball_2.draw(win)

ball_3 = Circle(Point(500,300), RADIUS)
ball_3.setFill("Navy")
ball_3.setOutline("Black")
ball_3.setWidth(3)
ball_3.draw(win)

while (1):
    
    # Sets up speed of each circle
    ball_1.move(4*xDir1,0)
    ball_2.move(4*xDir2,0)
    ball_3.move(4*xDir3,0)
    
    # Checks if circle come into contact with wall
    # and changes their direction
    if  ball_1.getCenter().getX() < RADIUS:
        xDir1 *= -1
    elif ball_3.getCenter().getX() > WIN_SIZE-RADIUS:
        xDir3 *= -1
    
    # Calculates distance between circles to detect
    # collision
    ball_1_X = ball_1.getCenter().getX()
    ball_1_Y = ball_1.getCenter().getY()
    ball_2_X = ball_2.getCenter().getX()
    ball_2_Y = ball_2.getCenter().getY()
    ball_3_X = ball_3.getCenter().getX()
    ball_3_Y = ball_3.getCenter().getY()
    collision_1 = math.sqrt((ball_1_X-ball_2_X)**2 + (ball_1_Y-ball_2_Y)**2)
    collision_2 = math.sqrt((ball_2_X-ball_3_X)**2 + (ball_2_Y-ball_3_Y)**2)
    
    # Changes circle direction based upon a collision of 
    # two circles
    if collision_1 < 2*RADIUS: 
        xDir1 *= -1
        xDir2 *= -1
    if collision_2 < 2*RADIUS:
        xDir2 *= -1
        xDir3 *= -1
        
    update(UPDATE_RATE)
     
win.getMouse()
win.close()