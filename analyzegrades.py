"""
Author: Leigh Stauffer
Project Number: 6-5
File Name: analyzegrades.py

This program obtains a list of integer grades from a given file, filters and
drops any grades less than 70, sorts them in descending order, and prints both
the sorted grades and their average.
"""
from myfunctions2 import inputList


def main():
    grades = inputList("Enter a grade", int)
    grades = list(filter(lambda n: n >= 70, grades))
    grades.sort (reverse = True)
    average = sum(grades) / len(grades)
    print ("Grades are: ", grades)
    print ("Average grade: " + str(average))
    
if __name__ == "__main__":
    main()
