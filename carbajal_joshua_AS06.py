# File Name: carbajal_joshua_AS06.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS06.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS06.py

# Joshua Carbajal
# Date (10/10/19)
# AS.06
# Median Function
# Purpose: Function that takes a list of numbers as an argument and prints
# 	       the median value.

numList = [1, 3, 5, 7, 9, 2, 4, 8, 0, 4]

# Function used to find median value of a list of numbers
def median(numList):
    numList.sort() #Sorts list in ascending order
    print(numList)
    n = len(numList)
    if n % 2 != 0: # Odd number of integers
        val = (n + 1) // 2
        medVal = numList[val-1]
        print("The median value is " + str(medVal))
    else: # Even number of integers
        val_1 = (n // 2) - 1 # Gets first index value
        value1 = numList[val_1]
        val_2 = (n // 2) # Gets second index value
        value2 = numList[val_2]      
        medVal = (value1 + value2) / 2 # Finds the average of those index values
        print("The median value is " + str(medVal))
	
	
median(numList)
	
	
