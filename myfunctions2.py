"""
Author: Leigh Stauffer
Project 6-1, 6-2, 6-3, 6-4
File: myfunctions2.py

Defines the functions inputList, isSorted, and myRange.
"""

from random import shuffle

# New function definitions go here
def inputList(prompt, convert = str):
    """
    Arguments: user string and optional type conversion function
    Returns: a list of inputs as
    """
    result = []
    
    while True:
        data = input(prompt + " or return to quit: ")
        if data == "":
            return result
        result.append(convert(data))

def isSorted(lyst):
    """
    Arguments: list of comparable values
    Returns true if list values are in ascending order; otherwise, returns
    False.
    
    *Note: an empty list is considered to be sorted
    """
    if len(lyst) == 0:
        return True
    else:
        for i in range(len(lyst)-1):
            if lyst[i] > lyst[i+1]:
                return False
        return True

def myRange(first, second = None, third = None):
    """
    Behaves like Python's standard range function, but returns a list to the
    user.
    Arguments: fist (lower bound), second (upper bound), and third (step).
    Returns: list from first to second increasing by increments of third.
    """
    result = []
    if second == None and third == None:
        upper = first
        lower = 0
        step = 1
    elif third == None:
        lower = first
        upper = second
        step = 1
    else:
        lower = first
        upper = second
        step = third
    while lower < upper:
        result.append(lower)
        lower += step
    return result   

#Main function for testing
def main():
    """Tests the 3 functions."""
    ints = inputList("Enter an integer", int)
    floats = inputList("Enter a float", float)
    names = inputList("Enter a name")
    print("Ints:", ints)
    print("Floats:", floats)
    print("Names:", names)
    lyst = list(range(5))
    print("Lyst:", lyst)
    print("Expect True:", isSorted(lyst))
    shuffle(lyst)
    print("Lyst:", lyst)
    print("Expect False:", isSorted(lyst))
    lyst = myRange(6)
    print("Expect [0, 1, 2, 3, 4, 5]:", lyst)
    lyst = myRange(1, 7)
    print("Expect [1, 2, 3, 4, 5, 6]:", lyst)
    lyst = myRange(1, 7, 2)
    print("Expect [1, 3, 5]:", lyst)

if __name__ == "__main__":
    main()
