# def func():
#     """
#     This is a docstring
#     We can write what the function does here
#     :return: None
#     """
#     return None
#
# # func()
# print(help(func))

def divide(num1, num2):
    """
    num1: A number to be divided [Numerator]
    num2: A number that divides num1 [Denominator]
    :return: float (if num2 is non-zero) OR str (if num2 is 0)
    """
    if num2 ==0:
        return "Cannot divide as Denominator is 0"
    else:
        result = num1 / num2
        return result

help(divide)
print(divide(10, 2))
