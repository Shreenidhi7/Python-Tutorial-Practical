# User-Defined Function

"""
Syntax - User Defined Functions
def function_name(arg1,arg2,...,argN):
    statement1
    statement2
    ...
    statementN
"""

def checkEvenOrOdd(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

number = int(input("Enter a number: "))
checkEvenOrOdd(number)


