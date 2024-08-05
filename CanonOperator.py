# CanonOperator.py
"""
Title
Author
Date
"""
# =========================================================================================================
# IMPORT
import math
from z_myfunc import *

# =========================================================================================================
# VARIABLES
GRAVITY = 9.81
SCENARIO = 0

# =========================================================================================================
# DEFINITIONS

def scenario():
    print("""
=============================================================
    0. All aspects of the following scenarios
    
    Angle Diagram
    
    90 
    |       45
    |    __/
    | __/
    |/_________ 0
    |\\_
    |   \\_
    |      \\
    -90       -45
=============================================================
    1. Horizontal to the Water
    ____
    |   \\
    |    \\
    |     \\
=============================================================
    2. Parabolic to a level boat
       ____
      /   \\
     /     \\
    /       \\
=============================================================
    3. Parabolic to a smaller boat far away
      ____
     /    \\
     |    |
    /      \\
    |      |
=============================================================
    
    """)
    global SCENARIO
    SCENARIO = input(print("Please Enter Scenario Number 0, 1, 2, 3 "))


def scenario1():
    HEIGHT = input(print("Enter Height of Canon (m): "))
    HEIGHT = float(HEIGHT)
    SPEED = input(print('Enter Speed of Canon ball (m/s): '))
    SPEED = float(SPEED)

    TIME = ((2 * HEIGHT) / GRAVITY) ** 0.5
    DISTANCE = TIME * SPEED
    print("")
    print(f" Time taken to hit the water is: {TIME} seconds |"
          f" Distance traveled by the canon ball is: {DISTANCE} meters")
    askContinue()
    if True:
        print("=======================================================")
        return scenario0()


def scenario2():
    SPEED = input(print("Enter speed of canon ball (m/s): "))
    SPEED = float(SPEED)
    ANGLE = input(print("Enter Angle along horizontal plane (degrees): "))
    ANGLE = float(ANGLE)

    RADIANS = math.radians(ANGLE)
    HSPEED = SPEED * math.cos(RADIANS)
    VSPEED = SPEED * math.sin(RADIANS)
    PTIME = VSPEED / GRAVITY
    DISTANCE = HSPEED * PTIME * 2

    print(f" Time taken to reach peak height is: {PTIME} seconds |"
          f" Total Distance traveled is: {DISTANCE} meters")
    askContinue()
    if True:
        print("=======================================================")
        return scenario0()


def scenario3():
    SPEED = input(print("Enter speed of canon ball (m/s): "))
    SPEED = float(SPEED)
    ANGLE = input(print("Enter Angle along horizontal plane (degrees): "))
    ANGLE = float(ANGLE)
    HEIGHT = input(print("Enter Height above/below enemy ship (+m above, -m below): "))
    HEIGHT = float(HEIGHT)

    RADIANS = math.radians(ANGLE)
    HSPEED = SPEED * math.cos(RADIANS)
    VSPEED = SPEED * math.sin(RADIANS)
    PTIME = VSPEED / GRAVITY
    PDISTANCE = (VSPEED ** 2) / (2 * GRAVITY)
    TIME = ((SPEED * math.sin(RADIANS)) + ((SPEED * math.sin(RADIANS)) ** 2 + (2 * GRAVITY * HEIGHT)) ** 0.5) / GRAVITY
    DISTANCE = HSPEED * TIME
    DTIME = TIME - PTIME

    print(f" Maximum height the canon ball would reach above the canon is: {PDISTANCE} meters")
    print(f" Time taken to reach peak height is: {PTIME} seconds | Time taken to hit enemy from peak height is: {DTIME}"
          f" Total Distance traveled is: {DISTANCE} meters")
    askContinue()
    if True:
        print("=======================================================")
        return scenario0()


def scenario0():
    SPEED = input(print("Enter initial speed of the canon ball (m/s): "))
    SPEED = float(SPEED)
    ANGLE = input(print("Enter Angle +(ANGLE above horizontal plane) -(ANGLE below horizontal plane): "))
    ANGLE = float(ANGLE)
    HEIGHT = input(print("Enter Height above/below enemy ship (+m above, -m below): "))
    HEIGHT = float(HEIGHT)

    RADIANS = math.radians(ANGLE)
    HSPEED = SPEED * math.cos(RADIANS)
    VSPEED = SPEED * math.sin(RADIANS)
    PTIME = VSPEED / GRAVITY
    PDISTANCE = (VSPEED ** 2) / (2 * GRAVITY)
    TIME = ((SPEED * math.sin(RADIANS)) + ((SPEED * math.sin(RADIANS)) ** 2 + (2 * GRAVITY * HEIGHT)) ** 0.5) / GRAVITY
    DISTANCE = HSPEED * TIME
    DTIME = TIME - PTIME
    print("=======================================================")
    print(f"Horizontal Speed: {HSPEED}m/s")
    print(f"Vertical Speed: {VSPEED}m/s")
    print(f"Time to Peak: {PTIME}s")
    print(f"Time from Peak: {DTIME}s")
    print(f"Peak Height from start: {PDISTANCE}m")
    print(f"Total flight time: {TIME}s")
    print(f"Total Distance {DISTANCE}m")
    print("=======================================================")
    askContinue()
    if True:
        print("=======================================================")
        return scenario0()

# =========================================================================================================


print("")
print("Welcome to Navy Canon Distance Calculator, Finds the Total Distance of Travel from the Canon. ")

scenario()
# =========================================================================================================
if SCENARIO == "0":
    scenario0()
elif SCENARIO == "1":
    scenario1()
elif SCENARIO == "2":
    scenario2()
elif SCENARIO == "3":
    scenario3()

# =========================================================================================================
