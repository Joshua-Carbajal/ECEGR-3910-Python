# File Name: carbajal_joshua_AS08.py
# File Path: /home/carbaja1/Python/Python/carbajal_joshua_AS08.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS08.py

# Joshua Carbajal
# Date (10/18/19)
# AS.08
# Target Practice
# Purpose: Creates a game on a graphic window utilizing an analog joystick. 
#          User moves a circle over a randomly placed target and presses the 
#          push button to fire.  If the circle is over the target the target 
#          disappears and a new randomly placed target appears.

from graphics import *

import RPi.GPIO as GPIO
import time
import random
import math
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

WIN_SIZE = 600
MAX_VALUE = 500
MIN_VALUE = 50
UPDATE_RATE = 30
RADIUS = 50
xDir = 4
yDir = 4
colorList = ["Blue", "Gold", "DarkRed", "DarkMagenta", "Gray", 
"Chocolate", "Indigo", "LightGreen", "DarkOrange"]
size = list(range(5,50))

# Setup GPIO
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering
GPIO.setup(16, GPIO.IN)
button_1 = False

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0 & 1
chan_0 = AnalogIn(mcp, MCP.P0)
chan_1 = AnalogIn(mcp, MCP.P1)

# Function for push button    
def buttonOne_callback(channel):
    global button_1
    button_1 = True

GPIO.add_event_detect(16, GPIO.FALLING, callback=buttonOne_callback, bouncetime=300)

win = GraphWin("Target Game", WIN_SIZE, WIN_SIZE)

# Draws the target on the graphic window
x_t = random.randint(MIN_VALUE, MAX_VALUE)
y_t = random.randint(MIN_VALUE, MAX_VALUE)
t = Circle(Point(x_t, y_t), random.choice(size))
tColor = random.choice(colorList)
t.setFill(tColor)
t.setWidth(3)
t.draw(win)

# Draws the sight reticle on the graphic window
r = Circle(Point(300,300), RADIUS)
r.setFill("DodgerBlue")
r.setOutline("Black")
r.setWidth(3)
r.draw(win)





while (1):
    #Sets the radius of the next target at random
    radiusTarget = random.choice(size)
    
    # Sets up the speed of the reticle
    voltage0 = round(chan_0.voltage, 1)
    voltage1 = round(chan_1.voltage, 1)
    x_speed = (voltage1-1.6)
    y_speed = (1.6-voltage0)
    
    
    
    # Creates border boundaries on graphics window
    if r.getCenter().getX() > WIN_SIZE-RADIUS:
        xDir *= -1
    elif r.getCenter().getX() < RADIUS:
        xDir *= -1
    elif r.getCenter().getY() > WIN_SIZE-RADIUS:
        yDir *= -1
    elif r.getCenter().getY() < RADIUS:
        yDir *= -1
    
    r.move(x_speed*xDir, y_speed*yDir)    
    update(UPDATE_RATE)
    
    # Checks distance between reticle and target circle to
    # determine if in proximity to on another when button is pushed
    r_X = r.getCenter().getX()
    r_Y = r.getCenter().getY()
    t_X = t.getCenter().getX()
    t_Y = t.getCenter().getY()
    d = math.sqrt((r_X-t_X)**2 + (r_Y-t_Y)**2)
    
    # Checks if reticle is over the target, if so and button is pushed
    # new target appears at random location.
    if d < 2*RADIUS and button_1:
        button_1 = False # Resets the button for next button push
        t.undraw()
        x_t = random.randint(MIN_VALUE, MAX_VALUE)
        y_t = random.randint(MIN_VALUE, MAX_VALUE)
        t = Circle(Point(x_t, y_t), radiusTarget)
        tColor = random.choice(colorList)
        t.setFill(tColor)
        t.setWidth(3)
        t.draw(win)
        r.undraw()
        r.draw(win)
        
        
          