"""
Write a program to simulate a roll of die/dice.
A die has 6 faces with numbers 1 to 6 written on them.
The program should randomly print a number between 1 and 6
"""

import random
print("Welcome to the game of rolling a dice")
while True:
    choice = input("Please 'Enter' to roll and dice or 'Quit' to quit: ")
    choice = choice.strip()
    if choice == "Quit":
        print("Thank you for playing the game, bye!")
        break
    elif choice == "Enter":
        number = random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print("Invalid input, please try again")