"""
Author: Leigh Stauffer
Program Number: 4-4
File Name: numberlines.py

This program numbers the lines of text in a file of the user's choice.  The
line numbers will be right justified. After the columns are numbered, the user's
file will be saved as a new file with the prefix "numbered" in front of the
originial file's name.
"""

#Obtain user's input file and renaming new output file.
userFile = input("Name of file: ")
inputFile = open( userFile, "r")
outputFile = open( "numbered" + userFile, "w")

#Starting line number count.
lineNumber = 0

#Adding line numbers.
for line in inputFile:
    lineNumber += 1
    outputFile.write( str('%4s  %s' % (lineNumber, line)))

#Closing and saving output file.
outputFile.close()
    
