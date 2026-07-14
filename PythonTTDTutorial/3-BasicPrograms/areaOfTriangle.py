"""
When all the length of the sides of the triangle is known - a, b, c
Formula:
Semi Perimeter (s) = (a + b + c)/2
Area of Triangle = square root of (s * (s-a) * (s-b) * (s-c))
"""

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
s = (a + b + c) / 2
print("The semi perimeter of the triangle is:", s)

area = s * (s - a) * (s - b) * (s - c) ** 0.5
print("The area of the triangle with given side is:", area)
# round it off to 2 decimal points
print("The area of the triangle with given side is:", round(area, 2))