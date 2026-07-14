"""
Recursion is a process in which a function calls itself till a certain condition is met
Factorial of n => n * (n-1) * (n-2) ....
representation of factorial => n!
4! = 4 * 3 * 2 * 1 = 24
"""

###############
# Without Recursion

# def fact(num):
#     factorial = 1                           # num=5, fact=1
#     while num >= 1:                         # num=5, 5>=1                   #num=4, 4>=1            #num=3,3>=1                 #num=2,2>=1                 #num=1, 1>=1                #num=0, 0 !>= 1
#         factorial = factorial * num         # factorial = 1*5 => 5          #5*4 => factorial=20    #20*3 => factorial=60       #60*2 => factorial=120      #120*1 => factorial=120
#         num = num - 1                       # num=num-1, 5-1=> 4, num=4     #4-1=3, num=3           #3-1=2, num=2               #2-1=1, num=1               #1-1=0, num=0
#     return factorial                        # factorial=120
#
# num = 5
# print(f"Factorial of {num} is {fact(num)}")


##################
# With Recursion
'''
There are 2 parts of the recursive function
1. Base/Terminal Condition
    - Deciding when the function should stop calling itself
2. Recursive Condition
    - How to function should call itself.
'''

"""
Factorial Example:
n! = n * (n-1) * (n-2) .... * 1
n! = n * (n-1)!
n! = n * (n-1) * (n-2)! ........
"""

"""
1. 1st write the base condition.
2. Next we write the logic on how function should call itself. 
"""

def fact_rec(number):
    if number == 1:
        return 1
    else:
        factorial = number * fact_rec(number - 1)
        return factorial
fact_number_rec = fact_rec(4)
print(fact_number_rec)

