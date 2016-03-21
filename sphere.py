"""
Author: Leigh Stauffer
Project 1
File name: sphere.py

This program calculates the diameter, circumference, surface area,
and volume of sphere.  The user simply needs to provide the radius.
Enjoy!

"""

import math

radius = float(input("Enter the radius of a sphere: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
surfaceArea = 4 * math.pi * radius ** 2
volume = 4/3 * math.pi * radius **3

print ("The diameter of the sphere is:", diameter)
print ("The circumference of the sphere is:", circumference)
print ("The surface area of the sphere is:", surfaceArea)
print ("The volume of the sphere is:", volume)
