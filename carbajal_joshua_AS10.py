# File Name: carbajal_joshua_AS10.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS10.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS10.py

# Joshua Carbajal
# Date (10/24/19)
# AS.10
# Decision Making-Three Sort
# Purpose: Sort three unique random integers in ascending order and 
#          calculates the number of moves for 1000 sets of integers.

import random
import statistics

def sorty():
    data = []
    i = 0
    while i < 1000 :
        count = 0
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        c = random.randint(1, 50)
        
        count += 2
        if (a <= b and a <= c):
            count += 1
            if (b <= c):
                print(str(a), str(b), str(c))
            else:
                count += 1
                print(str(a), str(c), str(b))
        elif (b <= a and b <= c):
            count += 2
            count += 1
            if (a <= c):
                print(str(b), str(a), str(c))
            else:
                count += 1
                print(str(b), str(c), str(a))
        else:
            count += 1
            if (a <= b):
                print(str(c), str(a), str(b))
            else:
                count += 1
                print(str(c), str(b), str(a))
            
        i += 1
        data.append(count)
    
    average = statistics.mean(data)
    print()
    print("Average number of moves on 1000 sets of numbers is: " + str(average))

sorty()