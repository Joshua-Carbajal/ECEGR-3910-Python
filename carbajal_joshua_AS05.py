# File Name: carbajal_joshua_AS05.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS05.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS05.py

# Joshua Carbajal
# Date (10/13/19)
# AS.05
# Push Button
# Purpose: 2 buttons control on/off of an LED along with functionality to allow
#          LED to blink at different preset blink rates.

# Import Libraries
import RPi.GPIO as GPIO # Raspberry Pi GPIO library
import time # Time library

# Setup GPIO
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # Set Pin 4 to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.IN)
GPIO.setup(26, GPIO.IN)

blink_rate = [0, 2, 1, 0.2, 0.1] # Blink rates for button two
blinky = 0 # Constant variable for blink rate index
count = 0 # Constant variable for blink rate indexing
button_1 = False

# Function controls button one. Turns the LED
# on and off and resets the blink rate to setting zero.
def buttonOne_callback(channel):
    global blinky
    global count 
    global button_1   
    if (GPIO.input(4) == 1):
        GPIO.output(4, GPIO.LOW)# If LED is on, turns it off
        button_1 = False # Sets boolean to false so LED does not continue blinking
    else:
        GPIO.output(4, GPIO.HIGH)# If LED is off, turns it on
        blinky = blink_rate[0] # Resets the blink rate to setting zero
        count = 0 # Resets the counter 
 
# Function controls the blink rate of the LED 
def buttonTwo_callback(channel):
    global blinky
    global count
    global button_1
    button_1 = True # Allows while loop to iterate through
    count += 1 # Increments by one for blink rate indexing
    if (count % 5 != 0):
        blinky = blink_rate[count % 5] #Indexes the blink rate to appropriate value
    else:
        blinky = blink_rate[0] #Returns blink rate back to setting zero
    

# Add event detectors
GPIO.add_event_detect(16, GPIO.FALLING, callback=buttonOne_callback, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=buttonTwo_callback, bouncetime=300)

# While loop used for LED blink. Breaks out of loop if button one is pushed.
while(1):
    if(button_1 == True):
        GPIO.output(4, GPIO.LOW) # LED off
        time.sleep(blinky) # sleep       
        GPIO.output(4, GPIO.HIGH) # LED on 
        time.sleep(blinky) # sleep 



try:
# Setup infinite loop
    while(1): 
        time.sleep(1e6) # Sleep and wait for button detects

except KeyboardInterrupt: 
    # This code runs on a Keyboard Interrupt <CNTRL>+C
    print('\n\n' + 'Program exited on a Keyboard Interrupt' + '\n') 

except: 
    # This code runs on any error
    print('\n' + 'Errors occurred causing your program to exit' + '\n')

finally: 
    # This code runs on every exit and sets any used GPIO pins to input mode.
    GPIO.cleanup()