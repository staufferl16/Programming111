"""
Author: Leigh Stauffer
Project 3-1
File: game.py

This program plays a guessing game with the user.  The program thinks of a
number between 1 and 100.  The user inputs guesses until a guess equals the
number. The program then displays the total number of guesses.  However, if
the user is unable to correctly guess the program's number within 7 guesses,
it's "Game Over!"
"""

import random

myNumber = random.randint(1, 100)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    if userNumber > myNumber:
        print("Too large!")
    if userNumber == myNumber :
        print("You got it in", count, "tries!")
        break
    if count > 6:
        print( "You've exceeded your guesses: GAME OVER!")
        break
