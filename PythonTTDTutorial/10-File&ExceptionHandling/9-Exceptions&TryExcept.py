"""
Compile Time Error
1. Syntax Error
2. Indentation Error
"""

## Syntax Error
# age = 24
# print(age

# ## Indentation Error
# age = 24
# if age >= 18:
# print(age)


## Exceptions
# print(10/0)
# x = 100
# result = x+y


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# try:
#     result = num1 / num2
#     print(result)
# except:
#     print("The denominator cannot be equal to zero")

# try:
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("The denominator cannot be equal to zero")


#############

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("The denominator is zero")