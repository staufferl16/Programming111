"""
Author: Leigh Stauffer
Project Number: 4-1
File Name: filestats.py

This program prompts the user for a file name and outputs the number of
characters, words, and lines in the file.  If the file does not exist, however,
the program will retrun an "ERROR: File does not exist!" message.

"""
#Import necessary files to use the isfile function
import os.path

#Gather inputs and set temporary variables for calculations about file stats
fileName = input( "Enter the file name: ")
word = 0
character = 0
lines = 0

#Performing functions for calculating and printing the file stats
if not os.path.isfile(fileName):
    print( "ERROR: the file does not exist!")
else:
    inputFile = open( fileName, "r")
    for line in inputFile:
        character += len( line)
        word += len( line.split())
        lines += 1
    print( "There are", character, "characters.")
    print( "There are", word, "words.")
    print( "There are", lines, "lines.")
