"""
Author: Leigh Stauffer
Project: 3 - 3
File: leibniz.py

This program approximates the value of pi.  The user specifies the number of
iterations used for calculating the resulting approximation.  For
comparison purposes, Python's own math.pi will be displayed, as well.

Note: user input for iteration must be greater than 0!
"""

#Importing math.pi for later comparison with output
import math

#Create starting point
sign = 1
summation = 0

#Obtain user inputs
iteration = int( input("Number of iterations: "))
if iteration <= 0 :
    print ("Error: user input must be greater than 0!")

#Instructing computer on how to conduct the summation
for n in range (1, iteration + 1):
    denominator = 2 * n - 1
    summation = summation + (sign) * (1/denominator)
    sign = -1 * sign


#print result
print ("Your approximation of pi: ", 4 * summation)
print ("Python's approximation of pi: ", math.pi)


