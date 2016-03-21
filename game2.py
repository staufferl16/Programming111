"""
Author: Leigh Stauffer
Project 3-2
File: game2.py

This program allows the computer to play a guessing game with the user.  The
user thinks of a number between 1 and 100, and the computer will respond with
a guess.  If the computer's guess is wrong, then the user must respond
appropriately with either <Too small!> or <Too large!>.  The computer will
proceed to make educated guesses until it guesses correctly.
"""
#Assigning initial varbiables for first guess.
high = 100
low = 0

#Instructing the computer on how to guess.    
while True :
    guess = (low + high) // 2
    print("My guess is", guess)
    hint = input( "High, Low, or Correct? ")
    if hint == "High" :
        high = guess - 1
    if hint == "Low" :
        low = guess + 1
    elif hint == "Correct" :
        print( "Hooray!!  Thanks for playing, pal!")
        break
