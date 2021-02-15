# File Name: carbajal_joshua_AS13.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS13.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS13.py

# Joshua Carbajal
# Date (10/24/19)
# AS.09
# Nested Loops Practice 
# Purpose: 

# Part 1
print("Part 1")
for i in range(0,5):
    for j in range(0,5):
        print('*', end='')
        print(' ', end='')
    print()
    
# Part 2
print("Part 2")

HEIGHT = 5
for i in range(1,HEIGHT):
    for j in range(i):
        print('*', end='')
        print(' ', end='')
    print()
    
for i in range(HEIGHT, 0, -1):
    for j in range(i):
        print('*', end='')
        print(' ', end='')
    print()

# Part 3
print("Part 3")

WIDTH = 10
for a in range(1, WIDTH+1):
    for b in range(WIDTH-a, 0, -1):
        print(' ', end='')
    for c in range(a):
        print('*', end='')
        print(' ', end='')
    for d in range(WIDTH-a, 0, -1):
        print(' ', end='')
    print()
   
for a in range(WIDTH-1, 0, -1):
    for b in range(WIDTH-a, 0, -1):
        print(' ', end='')
    for c in range(a):
        print('*', end='')
        print(' ', end='')
    for d in range(WIDTH-a, 0, -1):
        print(' ', end='')
    print()
   
    
 


     
