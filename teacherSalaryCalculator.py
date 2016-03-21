"""
Name:  Leigh Stauffer
Project Number:  2-1
File Name:  Teacher Salary Calculator.py

This program calculates the salary of a teacher, who is teaching
in a typical school district, based on the number of years for which he or
she has consecutively taught.  This formula applies for a teacher who has been
teaching for up to 10 years.  After 10 years, the salary stops increasing.

The user must provide: the number of teaching years, the starting salary, and
the annual percentage increase.

Cha-ching!

"""



#User inputs variables that will be used for calculating teacher salary.
income = float(input( "Enter your starting income: "))
yearsOfTeaching = int(input( "Enter years of teaching: "))
salaryIncreaseRate = float(input( "Enter salary increase rate: "))

#Column Lables for outputs
for x in range (1):
    print( "%-7s%10s" % ("Year", "Salary"))


#Printing outputs for user to see.

for year in range (yearsOfTeaching) :
    print( "%-3d%14.2f" % (year, income))
    income = income + salaryIncreaseRate * income
