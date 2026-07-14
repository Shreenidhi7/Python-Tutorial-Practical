# Syntax of IF-ELSE
#	- if condition:
#		- block of code to be executed when the condition is True
#	- else:
#		- block of code to be executed when the condition if False

# age = float(input("What is your age? "))
# if age >= 18:
#     print("Congrats! You can cast your vote!")
# else:
#     print("A few more years before you can vote")
#
# print("Reset of the program")

######################
# Write a program to print if a number (int) is odd or even
# even - when number is divisible by 2 - if the reminder is zero
# odd - when number is not divisible by 2 - if the reminder is non-zero

# num = int(input("Enter a integer number: "))
# if num % 2 == 0:
#     print(f"The number {num} is even")
# else:
#     print(f"The number {num} is odd")

#######################
# Write a logic to print if a number is negative or positive
num = float(input("Enter a number: "))

if num > 0:
    print(f"The number {num} is positive")
elif num < 0:
    print(f"The number {num} is negative")
else:
    print(f"The number {num} is zero")