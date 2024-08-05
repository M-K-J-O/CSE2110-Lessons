#c_calculator2.py
"""
Title
Authro
Date
"""
import math
from z_myfunc import *
### functions
def intro():
    """
    Display program instructions to the user
    :return: (none)
    """
    print("Welcome to my Calculator")

### inputs
def menu():
    """
    User selects which math operation to perform
    :return: (int)
    """
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. sin(X)
    """)
    CHOICE = checkInt(input("> "))
    if CHOICE > 0 and CHOICE < 6:
        return CHOICE
    else:
        print("Please choose a number in the menu! ")
        return menu()

def askNum(ORDER):
    """
    Asks user for a number
    :param ORDER: (str)
    :return: (float)
    """
    NUMBER = input(f"Please enter the {ORDER} number: ")
    return checkFloat(NUMBER)

def Calculatoraddition():
    FIRST = askNum("first")
    SECOND = askNum("second")
    ANSWER = FIRST + SECOND
    print(FIRST, "+", SECOND, "=", ANSWER)
    askContinue()
    if True:
        return menu()
    else:
        exit(0)
def Calculatorsubtraction():
    FIRST = askNum("first")
    SECOND = askNum("second")
    ANSWER = FIRST - SECOND
    print(FIRST, "-", SECOND, "=", ANSWER)
    askContinue()
    if True:
        return menu()
    else:
        exit(0)
def Calculatormultiplication():
    FIRST = askNum("first")
    SECOND = askNum("second")
    ANSWER = FIRST * SECOND
    print(FIRST, "*", SECOND, "=", ANSWER)
    askContinue()
    if True:
        return menu()
    else:
        exit(0)
def Calculatordivision():
    FIRST = askNum("first")
    SECOND = askNum("second")
    ANSWER = FIRST / SECOND
    print(FIRST, "/", SECOND, "=", ANSWER)
    askContinue()
    if True:
        return menu()
    else:
        exit(0)
def CalculatorSin():
    """
    Calculates the Sin trig ratio of an angle
    :param Num: (float) degrees
    :return: (float)
    """
    degree = askNum("first")
    RADIANS = math.radians(degree)
    ANSWER = math.sin(RADIANS)
    print (ANSWER)
    askContinue()
    return ANSWER



### processing





### outputs




### Main Code

intro()
CHOICE = menu()
if CHOICE == 1:
    Calculatoraddition()
if CHOICE == 2:
    Calculatorsubtraction()
if CHOICE == 3:
    Calculatormultiplication()
if CHOICE == 4:
    Calculatordivision()
if CHOICE == 5:
    CalculatorSin()

"""
if CHOICE == 2:

if CHOICE == 3:

if CHOICE == 4:

if CHOICE == 5:

if CHOICE == 6:
"""





























































































