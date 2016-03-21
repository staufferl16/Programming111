"""
Author: Ken Lambert
Project 7
File: turtleexamples.py

Defines some functions to draw geometric shapes in turtle graphics.
"""

import random
from turtle import Turtle

def drawSquare(t, length):
    """Draws a square with length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

def drawPentagon(t, length):
    """Draws a pentagon with length."""
    for count in range(5):
        t.forward(length)
        t.left(72)

def drawFlower(t, length):
    """Draws a flower with length."""
    for petals in range(36):
        drawSquare(t, length)
        t.left(10)

# Microprogram to test functions

def main():
    """This is run only when F5 is pressed from IDLE or when
    this file is run as a script in a terminal window."""
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("blue")
    drawSquare(t, 50)
    drawPentagon(t, 50)
##    drawFlower(t, 50)
##    for sides in range(3, 7):     # Draw triangle, square, pentagon, hexagon
##        drawShape(t, 50, sides)
##    drawShape(t, 50, 8)                 # Draw octagon
##    drawFlower(t, 50)                   # Flower with 4 squares
##    drawFlower(t, 50, 10)               # Flower with 10 squares
##    drawFlower(t, 50, 6, drawPentagon)  # Ditto
##    drawFlower(t, 50, 4, lambda t, length: drawShape(t, length, 8)) # 4 octagons
    
if __name__ == "__main__":
    main()
