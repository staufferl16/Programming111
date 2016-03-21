"""
Name: Leigh Stauffer
Project number: 2-2
Program name: bouncyBallCalculator.py

This program allows the user to calculate the total distance a ball will bounce
upon being dropped from a given height.  The user must provide the initial
height from which the ball is being dropped, the ball's bounciness index, and
the number of times the ball is allowed to bounce.

"""

#User gives inputs for calculation
height = float( input( "Initial drop height: "))
bouncinessIndex = float( input( "Bounciness index: "))
numberOfBounces = int( input( "Number of bounces: "))

#New variable for distance traveled.
distance = 0


#Calculating and printing the total distance traveled for user to view.
for bounces in range (numberOfBounces):
    distance = height + bouncinessIndex * height + distance
    height = bouncinessIndex * height

print ("Total distance traveled: " + str(distance))
