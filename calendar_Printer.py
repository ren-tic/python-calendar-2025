# Filename: calendar_Printer.py
# Author: Lauren Wu
# Date Created: 2/28/25
# Description of Program: Calendar Printer App For Each Month Of 2025!

JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

MONTHS_dict = {

    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"

}

DAYS_dict = {

    0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
    4: "Thursday", 5: "Friday", 6: "Saturday"

}

DAYSflipped_dict = {

    "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, 
    "Friday": 5, "Saturday": 6

}

firstDayOfMonth_dict = {

    1: "Wednesday", 2: "Saturday", 3: "Saturday", 4: "Tuesday", 5: "Thursday", 6: "Sunday",
    7: "Tuesday", 8: "Friday", 9: "Monday", 10: "Wednesday", 11: "Saturday", 12: "Monday"
    
}

daysInMonth_dict = {

    1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:30,
    7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31

}

n = 0

def monthName_1( n ):
    """Damn I sure hope this works lol!"""

    return MONTHS_dict[n]

def monthName_old( n ):
    """Given the number of a month, returns its name.  Assumes that n is in
    range [1..12].

    """
    if (n == JAN):
        return "January"
    elif (n == FEB):
        return "February"
    elif (n == MAR):
        return "March"
    elif (n == APR):
        return "April"
    elif (n == MAY):
        return "May"
    elif (n == JUN):
        return "June"
    elif (n == JUL):
        return "July"
    elif (n == AUG):
        return "August"
    elif (n == SEP):
        return "September"
    elif (n == OCT):
        return "October"
    elif (n == NOV):
        return "November"
    elif (n == DEC):
        return "December"

def firstDayOfMonth_1( n ):
    """Woopee"""
    return firstDayOfMonth_dict[n]

def firstDayOfMonth_old( n ): 
    """Given a month in 2025, yields which day (represented by a number) it begins on.
    Example, if n == JAN, returns WED (i.e, 3), since January, 2025
    began on Wednesday (day 3).  Days are numbered from [0...6].

    """
    if (n == JAN):
        return WED
    elif (n == FEB):
        return SAT
    elif (n == MAR):
        return SAT
    elif (n == APR):
        return TUE
    elif (n == MAY):
        return THU
    elif (n == JUN):
        return SUN
    elif (n == JUL):
        return TUE
    elif (n == AUG):
        return FRI
    elif (n == SEP):
        return MON
    elif (n == OCT):
        return WED
    elif (n == NOV):
        return SAT
    elif (n == DEC):
        return MON

def daysInMonth2025_1( n ):
    return daysInMonth_dict[n]

def daysInMonth2025_old( n ):
   """Returns the number of days in a given month of the year 2025. For example, daysInMonth2025(JAN) = 31.
   """
   if (n == JAN):
        return 31
   elif (n == FEB):
        return 28
   elif (n == MAR):
        return 31
   elif (n == APR):
        return 30
   elif (n == MAY):
        return 31
   elif (n == JUN):
        return 30
   elif (n == JUL):
        return 31
   elif (n == AUG):
        return 31
   elif (n == SEP):
        return 30
   elif (n == OCT):
        return 31
   elif (n == NOV):
        return 30
   elif (n == DEC):
        return 31

def printCalendarMonth_1( n ):
    
    titleLine = monthName_1( n ) + ", 2025"
    daysLine = "Su Mo Tu We Th Fr Sa"
    columnCounter = 0

    print("")

    print(titleLine.center(20))
    print(daysLine)
    
    columnCounter = DAYSflipped_dict[firstDayOfMonth_1(n)]

    print("   " * DAYSflipped_dict[firstDayOfMonth_1(n)], end="")

    for i in range(1, daysInMonth2025_1( n ) + 1):

        print(f"{i:2d} ", end="")
        columnCounter += 1
        if (columnCounter == 7):
            print()
            pass
            columnCounter = 0
        elif (columnCounter != 7):
            pass
    print("\n")

def printCalendarMonth_old( n ):
    """Prints the calendar for the month n for 2025 where n is in range
    [1..12]."""

    titleLine = monthName_old(n) + ", 2025"
    daysLine = "Su Mo Tu We Th Fr Sa"
    columnCounter = 0 

    #no more variables

    print("")

    print(titleLine.center(20))
    print(daysLine)
    
    columnCounter = firstDayOfMonth_old(n)

    print("   " * firstDayOfMonth_old(n), end="")

    for i in range(1, daysInMonth2025_old( n ) + 1):

        print(f"{i:2d} ", end="")
        columnCounter += 1
        if (columnCounter == 7):
            print()
            pass
            columnCounter = 0
        elif (columnCounter != 7):
            pass
    print("\n")

def main_1():
    print("Welcome to our calendar utility!")
    print("Print the calendar for any month in 2025.")
    print()
    while True:
        n = input("Enter a month [1..12] or 0 to stop: ")

        if n.isdigit():
            n = int(n)
            if (1 <= n <= 12):
                printCalendarMonth_1(n)
            elif n == 0:
                print("Thanks for visiting! Goodbye!")
                break
            else:
                print("Month must be a number between 1 and 12, or 0 to stop. Try again.", "\n")
        else: 
            print("Month must be a number between 1 and 12, or 0 to stop. Try again.", "\n")

def main_old():
    """Runs a loop accepting from the user month numbers.  Prints the
    calendar for each month requested from 2025.  Stops when the user
    enters 0.  Validates user input and allow multiple tries if the
    user enters invalid inputs.
    """
    
    print("Welcome to our calendar utility!")
    print("Print the calendar for any month in 2025.")
    print()
    while True:
        n = input("Enter a month [1..12] or 0 to stop: ")

        if n.isdigit():
            n = int(n)
            if (1 <= n <= 12):
                printCalendarMonth_old(n)
            elif n == 0:
                print("Thanks for visiting! Goodbye!")
                break
            else:
                print("Month must be a number between 1 and 12, or 0 to stop. Try again.", "\n")
        else: 
            print("Month must be a number between 1 and 12, or 0 to stop. Try again.", "\n")

main_1()
#main_old()