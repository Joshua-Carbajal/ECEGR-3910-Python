# File Name: carbajal_joshua_AS03.py
# File Path: /home/carbaja1/Python/carbajal_joshua_AS03.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS03.py

# Joshua Carbajal
# Date (10/02/19)
# AS.03
# Magic 8-Ball
# Purpose: Asks the user to provide a yes/no question and chooses a 
#          response for the user from a pre-constructed list of answers
#          at random.

# Imported the random library to be able to utilize its methods
import random

# Create list of pre-constructed answers
eightBallAnswers = ["It is certain", "It is decidedly so", "Without a doubt", 
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", 
"Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", 
"Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", 
"My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

# Ask the user for input
print() 
question = input("Ask the all-knowing 8-Ball any Yes/No question: ")

# Choose at random one response and print to the user
answer = random.choice(eightBallAnswers)
print()
print("Magic 8-Ball says...", answer)
print()