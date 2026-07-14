# # importing all the available functions from arithmetic module
# import ArithmeticModule
#
# # Using Add function from Arithmetic Module
# a = 100
# b = 20
# addition_result = ArithmeticModule.add(a, b)
# print(f"Addition of {a} and {b} is {addition_result}")
#
# # Using SquareRoot function from Arithmetic Module
# square_root_result = ArithmeticModule.square_root(a)
# print(f"Square root of {a} is {square_root_result}")
# square_root_result = ArithmeticModule.square_root(b)
# print(f"Square root of {b} is {square_root_result}")


# # importing specific functions from the arithmetic module
from ArithmeticModule import add
from ArithmeticModule import square_root

# Using Add Function
a = 100
b = 20
add_result = add(a, b)
print(f"Addition of {a} and {b} is {add_result}")

# Using SquareRoot function
squrt_result = square_root(a)
print(f"Square root of {a} is {squrt_result}")
sqrt_result = square_root(b)
print(f"Square root of {b} is {sqrt_result}")