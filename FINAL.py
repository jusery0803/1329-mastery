'''
 This program will be an encapsulation of some of the previous
 programs that we were working with.

 This will be a culmination of the program and be uploaded via Github.

 '''

#The full program will be that of a random chance game

#First we will import random dictionary for this game to work
from random import randint
import random

#Next we will prompt the user the premise of the game
print("Hello, and welcome to the random die roll game!\n\n")
print("You will roll the dice and if this matches the random number chose you win!")

#initiating the list of choices with the number of sides for the die
choices = [1,2,3,4,5,6]


#declaring an empty list so we can push a random number to
winner = []

#passing a random number
winner  = random.choice(choices)  #This will be the number to be checked to
check = randint(1,6)  #This will be the ranom generated number

#prompting the user for input to start the game

game = input("To start the game enter a 1 to begin and a 0 to stop: ")

while game == '1':
    print("\nThe winning number was: ", winner)
    
    if check == winner:  #This is checking if the random numbers match
        print("You rolled a: ", check)
        print("You win!!")
        winner = random.choice(choices)  #If matched, you must reset the numbers for multiple plays
        check = randint(1,6)
    else:
        print("You rolled a: ", check)
        print("Please try again\n")
        winner = random.choice(choices)

    game = input("\n\nTo try again enter a 1 if you want to quite enter a 0: ")

    

