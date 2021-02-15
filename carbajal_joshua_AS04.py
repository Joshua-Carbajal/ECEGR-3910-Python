# File Name: carbajal_joshua_AS04.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS04.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS04.py

# Joshua Carbajal
# Date (10/02/19)
# AS.04
# Into to For Loops
# Purpose: Ask user for input of a number that prints a list of colors
#          that are random and do not repeat themselves.

# Imported the random library to be able to utilize its methods
import random

# List created of all colors that can be chosen
colors = ["Candy Apple Red", "Burnt Amber", "Frost Turquoise", "Acapulco Blue", 
"Beige Mist", "Arcadian Blue", "Daytona Yellow", "Wimbledon White", "Rallye Red"
, "Sublime Green", "Hemi Orange", "Go Mango Orange", "Panther Pink", "Miami Blue", "Plum Crazy",
"Sunfire Yellow", "Grabber Green", "Hugger Orange", "Olympic Gold", "Charger Red"]

# User is asked for input on number choice
randNumber = input("Pick a number (1 - 20) from which to create a color list: ")
print()

# List is made and populated with non-repeating, random numbers with
# the size of the list the same as user input 
a = list(range(0,20))
randNumList = random.sample(a,int(randNumber))

# Printed list of random colors indexed from list of non-repeating
# random numbers
for i in range (0, int(randNumber), 1):
    val = randNumList[i]
    i += 1
    singleColor = colors[val]
    print(str(i) + "." + singleColor + "\n")
