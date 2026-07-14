"""
ASSIGNMENT 3:
Module 4: Functions & Modules in Python

Task 1: Calculate Factorial Using a Function

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

Expected Output:
For example, if the function is called with 5, it should return:
- Enter a number: 5
- Factorial of 5 is: 120
"""

# Factorial Using Loop
print(f"Factorial Using Loops")
def fact(num):
    factorial = 1                           # num=5, fact=1
    while num >= 1:                         # num=5, 5>=1                   #num=4, 4>=1            #num=3,3>=1                 #num=2,2>=1                 #num=1, 1>=1                #num=0, 0 !>= 1
        factorial = factorial * num         # factorial = 1*5 => 5          #5*4 => factorial=20    #20*3 => factorial=60       #60*2 => factorial=120      #120*1 => factorial=120
        num = num - 1                       # num=num-1, 5-1=> 4, num=4     #4-1=3, num=3           #3-1=2, num=2               #2-1=1, num=1               #1-1=0, num=0
    return factorial                        # factorial=120

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {fact(num)}")


# ##################
# With Recursion
print()
print(f"Factorial Using Recursion")
def fact_rec(number):
    if number == 1:
        return 1
    else:
        factorial = number * fact_rec(number - 1)
        return factorial

fact_number_rec = int(input("Enter a number: "))
factorial = fact_rec(fact_number_rec)
print(f"Factorial of {fact_number_rec} is {factorial}")
