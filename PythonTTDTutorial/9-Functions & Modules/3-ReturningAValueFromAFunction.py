# Returning a Value from a function

# def even_or_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# result = even_or_odd(5)
# print(result)

# def add(num1, num2):
#     result = num1 + num2
#     return result
#
# val_1 = int(input("Enter a number-1: "))
# val_2 = int(input("Enter a number-2: "))
# result = add(val_1, val_2)
# print(f"Result => {result}")

def arithmetic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return addition, subtraction, multiplication

val_1 = int(input("Enter a number-1: "))
val_2 = int(input("Enter a number-2: "))
result1, result2, result3 = arithmetic(val_1, val_2)
print(f"Addition => {val_1} + {val_2} = {result1}")
print(f"Subtraction => {val_1} - {val_2} = {result2}")
print(f"Multiplication => {val_1} * {val_2} = {result3}")