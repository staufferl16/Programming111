"""
Author: Leigh Stauffer
Project Number: 4-3
File Name: analyzeintegers.py

This program reads integers from a file of the user's choosing and displays the
number of integers in the file, the average of the integers, their minimum
value, and their maximum value.
"""
#Import programs for later use of their functions.
import math
import os.path

#Gather user input.
userText = input( "Name of file: ")

#Set temporary variables.
count = 0
summation = 0

#Open user's file.
f = open( userText, "r")

#Perform program's function
for line in f:
    wordList = line.split()
if len( wordList) > 0:
    currentMax = int(wordList [0])
    currentMin = int(wordList [0])
    for word in wordList:
        count += 1
        integer = int( word)
        summation += integer
        currentMin = min( currentMin, integer)
        currentMax = max(currentMax, integer)
    average = summation / count
    
#Print results
print( "Number of integers: ", count)
print( "Integers' Average: ", average)
print( "Integers' Maximum: ", currentMax)
print("Integers' Minimum: ", currentMin)    

