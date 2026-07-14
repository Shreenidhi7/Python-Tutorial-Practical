"""
Right Angled Triangle Calculation
2 sides are already given, need to find out the 3 side
Formula - 1/2 * b * h
without the 3rd side we can still calculate the area of triangle = 1/2 * b * h
"""

base_of_triangle = float(input("Enter the base of triangle: "))
height_of_triangle = float(input("Enter the height of triangle: "))

area = 1/2 * base_of_triangle * height_of_triangle
print("Area of Right Angled Triangle Calculation", area)
