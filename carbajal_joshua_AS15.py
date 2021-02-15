# File Name: carbajal_joshua_AS15.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS15.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS15.py

# Joshua Carbajal
# Date (11/3/19)
# AS.15
# Photo Booth
# Purpose: Program that takes 4 photos consecutively. A timer on the clock
#          display counts down before each photo is taken. Once they are taken 
#          they are stitched together, a border is placed around the image and 
#          a SU logo is placed at the bottom right corner. Finally the 
#          image is uploaded to Twitter.

import RPi.GPIO as GPIO # Raspberry Pi GPIO library
import time # Time library
from picamera import PiCamera # Camera library
from PIL import Image # Image library
from twython import Twython # Twitter library
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering

GPIO.setup(16, GPIO.IN) # Button input
camera = PiCamera()
camera.rotation = 180
button_1 = False
imageList = []
SIZE = 500
BORDER = 20
SIZE_LOGO = 100

# GPIO pins for each led segment that makes one digit
# correspond to segment a, b, c, d, e, f, g
led_segments = (27, 4, 22, 23, 13, 19, 17)

# Sets up each individual segment as output
for seg in led_segments:
    GPIO.setup(seg, GPIO.OUT) # Assigns each output LED
    GPIO.output(seg, 0) # Output set to 0

GPIO.setup(6, GPIO.OUT) # Assigns 4th digit LED as output
GPIO.output(6, 1) # Output set to 1

# Truth table for each number in a nested list
number = [[1,0,1,1,0,1,1], #5
	 [0,1,1,0,0,1,1], #4
	 [1,1,1,1,0,0,1], #3
	 [1,1,0,1,1,0,1], #2
	 [0,1,1,0,0,0,0], #1
	 [0,0,0,0,0,0,0]  #' '
	 ]

# Function for push button    
def buttonOne_callback(channel):
    global button_1
    button_1 = True
    
# Function to add logo to final image
def addLogo():
    imMerged = Image.open('/home/carbaja1/Desktop/mergedImage.jpg')
    logo = Image.open('/home/carbaja1/Desktop/SUinterlock.png')
    logo = logo.resize((SIZE_LOGO,SIZE_LOGO))
    x = (SIZE+BORDER*2)-(SIZE_LOGO+BORDER)
    y = (SIZE*4+BORDER*2)-(SIZE_LOGO+BORDER)
    imMerged.paste(logo, (x, y))
    imMerged.save('/home/carbaja1/Desktop/finalImage.jpg')

# Function to stitch all the images together and 
# adds a frame to the stitched image
def mergePhotos(imageList):
    width = SIZE+BORDER*2
    height = SIZE*4+BORDER*2
    mergedImage = Image.new("RGB", (width, height))
    for j in range(4):
        mergedImage.paste(imageList[j], (BORDER, SIZE*j+BORDER))
    mergedImage.save('/home/carbaja1/Desktop/mergedImage.jpg')    

# Function to upload photos to Twitter
def twitterUpload():
    # Fill in your keys and token infollowing variables 
    C_key = "Z8WmPjrVTPmhWptbIdy1BmCzr" 
    C_secret = "Qt62127YChSXmM3qgmLggzfCdtcUXuRvJBZ41S2Y8t2WL0HB6S" 
    A_token = "1191747179066449920-5nKy7fluHwa6zyxWeKJmYiFTMp1bRP" 
    A_secret = "rbRdWVQd5m40sV1bKRqwKmxVGZEXNOVJfFe7tPrGblDQT" 

    # Authenticate to your app.
    twitter = Twython(C_key,C_secret,A_token,A_secret) 

    # Tweet Photos 
    photo = open('/home/carbaja1/Desktop/finalImage.jpg', 'rb') 
    response = twitter.upload_media(media=photo)
    twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])    

# Function that provides a countdown timer before taking each picture
def timer():
    # Loops through numbers 5-0 on 1 digit display
    for ind_number in range(0, 6):
        for led in range(0, 7):
            GPIO.output(led_segments[led], number[ind_number][led])
        GPIO.output(6, 0)
        time.sleep(1)
        GPIO.output(6, 1)

GPIO.add_event_detect(16, GPIO.FALLING, callback=buttonOne_callback, bouncetime=300)

print("Push button starts the photo booth")
print()
while (1):
    if button_1: #button is pushed
        button_1 = False # Resets the button for next button push
        camera.resolution = (SIZE, SIZE)
        camera.start_preview()
        for i in range(4):
            timer()
            camera.capture('/home/carbaja1/Desktop/image%s.jpg' % i)   
            imageList.append(Image.open('/home/carbaja1/Desktop/image%s.jpg' % i))            
        camera.stop_preview()
        mergePhotos(imageList)
        addLogo()
        answer = input("Would you like to use the photo booth again?(Y/N) ")
        if answer.upper() == "N":
            print()
            twitterUpload()
            print("Thank you for using my photo booth! Photos uploaded to Twitter")
            break
        else:
            twitterUpload()
            del imageList[:] # Deletes list contents if user wants to run again
            continue
   
