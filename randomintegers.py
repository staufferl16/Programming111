"""
Author: Leigh Stauffer
Program Number: 4-2
File Name: randomintegers.py

This program outputs random integers to a text file.  The user provides the file
name and the number of random integers he or she wishes to output.
"""

#Import programs to later use their functions.
import random
import os.path

#Gather user inputs.
textFile = input( "Name of file: ")
integerNumber = int( input( "Number of random integers: "))

#Open user text file.
f = open( textFile, "w")

#Output random integers and close the document
for count in range (integerNumber):
    integer = random.randint( 1, integerNumber)
    f.write( str( integer) + "\n")
f.close()
