#a_intro.py
"""
TITLE
AUTHOR
DATE
"""

## Variables
### Procedural subroutines
print("Procedural subroutines with a local and global variables")

print("Exaple 1")

VAR = "Hello World"

print(VAR)

print("EXAmple 2")
def hello2():
    VAR = "Hellow Mr. World 2" #Local variable only affective inside of the subroutine
    print(VAR)
hello2()
print(VAR)

print("EXAMPEL #")
def hello3():
    global VAR #refrencing VAR in the main program
    VAR = "Hello Mr. World 3"
    print(VAR)

hello3()
print(VAR)

# terms
def mathEquation(NUMBER):
    RESULT = 4 * NUMBER + 5
    return RESULT

ANSWER = mathEquation(VALUE)
print(ANSWER)

#Value is the argument that goes into the nymber parameter and is transformed into the local variable result which is then returned and stored in the global variable ANSWER


















