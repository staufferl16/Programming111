"""
Author: Ken Lambert
Edited By:  Leigh Stauffer
File Name: testimages.py
Project: 8

Script for testing image processing functions.
"""

from images import Image

# Functions that transform images

def blackAndWhite(image):
    """Converts image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def detectEdges(image, amount):
    """Builds and returns a new image in which the 
    edges of the argument image are highlighted and
    the colors are reduced to black and white."""

    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()
    y = 0
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > amount or \
               abs(oldLum - bottomLum) > amount:
                new.setPixel(x, y, blackPixel)
            else:
                new.setPixel(x, y, whitePixel)
    return new

def posterize(image, triple = (0,0,0)):
    """This function converts the image to a color of the user's choosing and
    white."""
    
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, triple)
            else:
                image.setPixel(x, y, whitePixel)

def grayscale(image):
    """This function converts the colors of an image into a grayscale.  The
    grayscale displayed is psychologically accurate (the function considers
    luminance factors when calculating the gray value of each pixel)."""
    for y in range(image.getHeight() ):
        for x in range (image.getWidth() ):
            (r, g, b) = image.getPixel(x,y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            gray = r + g + b
            image.setPixel (x, y, (gray, gray, gray))

def sepia(image):
    """This function converts the colors of an image to produce a sepia
    effect."""
    grayscale(image)
    for y in range (image.getHeight() ):
        for x in range (image.getWidth() ):
            (red, green, blue) = image.getPixel(x,y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel (x, y, (red, green, blue))

def sharpen(image, degree, amount):
    """This function takes an image and makes the image seem as though its
    subjects' edges are more defined."""
    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3

    def darken(oldPixel):
        (r, g, b) = oldPixel
        return(max(r-degree,0), max(g-degree, 0), max(b-degree, 0))
    
    new = image.clone()
    y = 0
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > amount or \
               abs(oldLum - bottomLum) > amount:
                new.setPixel(x,y, darken(oldPixel))
    return new

# Tester functions

def testBlackAndWhite(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to black and white and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    blackAndWhite(image)
    image.draw()

def testDetect(name = "smokey.gif", amount = 20):
    """Loads and draws an image, then
    detects edges and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    image2 = detectEdges(image, amount)
    image2.draw()

def testPosterize(name = "smokey.gif", triple = (0,0,0)):
    """Loads and draws an image, then converts it to a color
    of the user's choosing and white, and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    posterize(image, triple)
    image.draw()

def testGrayscale(name = "smokey.gif"):
    """Loads and draws an image, converts it to pyschologically correct
    grayscale, and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    grayscale(image)
    image.draw()

def testSepia (name = "smokey.gif"):
    """Loads and draws an image, converts it to grayscale, then converts it to
    sepia, and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    sepia(image)
    image.draw()

def testSharpen (name = "smokey.gif", degree = 50, amount = 20):
    """Makes image appear crisper."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    image2 = sharpen(image, degree, amount)
    image2.draw()

# Code to run a tester function

def main():
##    testBlackAndWhite()
##    testDetect()
##    testPosterize()
##    testGrayscale()
##    testSepia()
    testSharpen()

if __name__ == "__main__":
    main()
        
