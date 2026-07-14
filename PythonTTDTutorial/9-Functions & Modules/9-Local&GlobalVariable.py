print("GLOBAL AND LOCAL VARIABLES")
n = 1   # GLOBAL VARIABLE

def fn():
    n = 5    # LOCAL VARIABLE
    print("in",n)
fn()

print("out",n)

print()
###########
print("GLOBAL VARIABLE")
n = 1   # GLOBAL VARIABLE

def fn():
    print("in",n)
fn()

print("out",n)


############
print()
"""
Important
- If we want to change the GLOBAL variable from the function, then there is a keyword in python called "global"
	- We can use this keyword to assign the local variable value to the global variable.
"""
print("ASSIGN LOCAL VARIABLE TO GLOBAL VARIABLE")
n = 1   # GLOBAL VARIABLE

def fn():
    global n
    n = 5    # LOCAL VARIABLE
    print("in",n)
fn()

print("out",n)
