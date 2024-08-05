#notes.md
#CSE2210 procedural programing

subroutines contain two different categories procedures and functions prcoedures are a seires of steps like following the steps of a recipe or a lab investigation In contrast finctions take some data as inputs called arugements and transforms the arguments into new data tge bew data can be returned at the end of the function the main difference between differnece between procedures and functions is that functions have their own inputs and outputs

## EX. 1 - Math Functions
Functions in programming are simmililar to functions in mathematics there are process where data is inputed into the fnction and a new result exits the function therefore an individual function can be considered a sub program to the program it will have its own inputs outputs processing and variables 
```python
f(x) = 4x + 5

```
| INPUTS | PROCESSING | OUTPUTS | 
| --- | --- | --- | 
| 0 | 4(0) + 5 | 5 |
| 1 | 4(1) + 5 | 9 |
| 2 | 4(2) + 5 | 13 |
| 3 | 4(3) + 5 | 17 |
```python
def myFunction(x):
    y = 4 * x + 5
    return y 

print(myFunction(4)) # displays 21
```



##Structure of a Function
```python
    def functionName(Paramenter1, Paramenter2, ...):
    #transformational code fpr the arguments inputted intp the parameters
    return VALUE
```

Creating a function uses the same statement as creating a procedural subroutine: ```def```. However functions also include pareameters within the parenthesis following the function name.

__ Arguemtns __ are external data number strings variable data structure etc. that are inputted into the parameter fromm the rest of the program the data is stored inside the funciton using the paramenter main instead of the argument main outside of the function.

Once rthe funciton compltes its processing with thei nput falues it can return a value back to the main program the main program will then need to tstore the returned value in a variable if it is needed furthere along the program return values can also include a statemetns that occurs on a single line for example (```return print(x)``) or typcasting (```return into(VAR)```)

A functino must have either an input or an output It **Does not**
require both.

### Variables in a Function 
In programming there are two differnet categories of variables global and local are accessed throughtout the main portion of non subroutine code local varaibles are accessed within a particlular subroutine local variables do not exist outside the subroutine in which they are used 
```python
def myFunction():
    localVar = 8
globalVar = 4


```

a Subroutine can call a global variable using a global stemten within a subroutine 
```python
globalVar = 4
def myFunction():
    global globalVar 

```

## advantages to functional programming 
functinal programming has many advantages over structure or top down programming
1. repeatablility which means that once the function is written it can be used in many differnet sections of the program without retying the same lines multiple times
2. modularity which means certain functions can be used and switched out for other functions without breaking the rest of the program
3. debugging and testing  where certain functions can be excluded from the main program until it is working propperly 
4. collaboration because local variables do not affect the rest of the main program multiple developers can be creating differnet functions and do not need to match variable names or data structures

## Returning multiple values from a function
A functino can have multiple return values in order to store all retyrn values seperate varaibles must be used or a more comlex data structure
```python
def myFunction():
    return VALUE1, VALUE2

VARIABLE1, VARIABLE 2 = myFunction()

```
## Doctstrings
\
Functions also use doctrings to descirbe what data is being inputted into the function and what data is expected to be outputted from the function doctstrings improve the readability of the program and is apart of the internal documentation 
```python
def ageCalculator(CURRENTY_YEAR, BIRTH_YEAR):
    """
    Calculates the age the user turns in the given year 
    Param: CURRENT_YEAR: (int) the year that we are calculating their age from 
    :param BIRTH_YEAR: (int) 
    :return: (int)
    """
```
## Recursive functions
recursive functions are functions that return to the same function this return value will only happen in certain instances and there is always a return value that is not the function
```python
def checkInt(NUMBER):
    """
    Verifies the number is an integer
    :param NUMBER: (String)
    :return: (int)
    """
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print("That is not a number!")
        NEW_NUM = input("Please enter a valid number: ")
        return checkInt(NEW_NUM)
```
ASIDE: While it is possible to call functions within other functions, using this technique heavily does not follow ipo well

## Using Multiple files
Subroutiens can be stored seperate files to organize funtions and improve colboration for example if you make a program to mage sales at a coffee shop functions can be organized into payments transactions and reports each of these categories can be seperate files imported into the main fil in this scenario deveiopers can then woek on seperate features of the program without disrupting other decelopers 

In order to link multiple files together python uses the import statement fules must be in the same folder or subfolder of the main porgram file 

the filename of the secondary files must follow variable naming converntions including being alphanumeric but not starting with a number and onlu isong hypens and underscores as special characters 

## default paramenters
function can have default arguments in the event that no arguments are passed itno othe function defaulte paramenters are often optional and are usually placed at the end of the function paramenters in descending order of importance

```python
#function with defautl parementers 
def myfunc(param1 = True):
    return param1

print(myfunc()) # display true
print(myfunc(False)) # display false
```

NOTE the function cannot skip default paramenters if there is a parameter lower in the list of parameters all default paramenters must have arguments to reaach the desired parameter 

### The \_\_name_\_\ magic variavle
when python runs a file it associates the main value to the name magic variable for the file that runs all other files imported into the running program use their file name as the main magic variable magic  varaibles are predetermined variables on the backend of the programming language that helps the program run otherwise programmers do not need to modifuy these values in the progarm magic variables are indicated ny two underscores before and after the test they are sometimes called double underscore variables or dunder variables since putoone automatically updates the name magic variable a check can be included to insure that codes run only if the given file is run not imported this check allows subroutines and functions to be tested in the respectile fules without the tests being imported into the main program 
```python
def somefunction(PARAM1):
    VALUE = # some code
    return VALUE 

if __name__ == "__main__:
    #this section will onlu run if this file is run not imported
print(someFunction(VARIA))
```



















