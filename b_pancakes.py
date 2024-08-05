# b_pancakes.py
"""
Title
Author
Date
"""
# SUBROUTINES
# INPUTS
def getFlour():
    """
    Asks the user for the amount of flour they have in cups
    :return: (float)
    """
    FLOUR = float(input("How many cups of flour do you have? "))
    return FLOUR
def getMilk():
    """
    Asks the user for the amount of millk they have in cups
    :return: (float)
    """
    MILK = float(input("How many cups of milk do you have? "))
    return MILK
def getEggs():
    """
    Asks the User how many eggs they have
    :return: (int)
    """
    EGGS = int(input("How many Eggs do you have? "))
    return EGGS
def getIngredients():
    """
    Asks the User how much flour (cups), milk (cups), and eggs they have
    :return: (float) (float) (int)
    """
    FLOUR = float(input("How many cups of flour do you have? "))
    MILK = float(input("How many cups of milk do you have? "))
    EGGS = getEggs()
    return FLOUR, MILK, EGGS
# PROCESSING
def makePancakes(FLOUR, MILK, EGGS):
    """
    Makes pancakes with flour eggs and milk 
    :param FLOUR: (float)
    :param MILK: (float)
    :param EGGS: (int)
    :return: (int) Number of servings we can make
    """
    if FLOUR < 1.5 or MILK < 1 or EGGS < 2:
        return 0
    else:
        FLOUR_SERVINGS = FLOUR // 1.5
        MILK_SERVINGS = int(MILK)
        EGGS_SERVINGS = EGGS // 2

        SERVINGS = FLOUR_SERVINGS
        if MILK_SERVINGS < SERVINGS:
            SERVINGS = MILK_SERVINGS
        if EGGS_SERVINGS < SERVINGS:
            SERVINGS = EGGS_SERVINGS
        return int(SERVINGS)
# OUTPUTS
def displayerPancakes(DOZEN):
    """
    Displays the total number of pancakes we can make
    :param DOZEN: (int)
    :return: (None)
    """
    if DOZEN == 0:
        print("You do not have enough ingredients to make pancakes!")
    else:
        PANCAKES = 12 * DOZEN
        print(f"You can make {PANCAKES} pancakes!!")

def displayPancakesDozen(DOZEN):
    """
    Displays how man dozens of pancakes the user can make
    :param DOZEN:
    :return: (None)
    """

    if DOZEN == 0:
        print("You can not make any Pancakes!~ ")
    else:
        print(f"You can make {DOZEN} dozen pancakes")
# MAIN CODE
# inputs
# FLOUR = getFlour()
# MILK = getMilk()
# EGGS = getEggs
FLOUR, MILK, EGGS = getIngredients()
"""
print(FLOUR, " Cups of Flour")
print(MILK, " Cups of Milk")
print(EGGS, " Eggs")
"""
# processing
SERVINGS = makePancakes(FLOUR, MILK, EGGS)
# outputs
print(f"You can make {SERVINGS} of Pancakes")
