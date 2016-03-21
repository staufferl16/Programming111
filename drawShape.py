"""
Author: Leigh Stauffer
Project Number: 7-1
File Name: drawShape.py

This functions expects a turtle, the length of a side, and the number of sides
as arguments, and draws the corresponding shape.
"""

from turtle import Turtle

def drawShape (t, length, sides):
    for count in range (sides):
        t.forward (length)
        angle = sides / 360
        t.left (angle)


