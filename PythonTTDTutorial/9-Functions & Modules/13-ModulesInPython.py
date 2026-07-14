# .py file is a module
# Built-In Modules
## math, random, datetime, ....

# how to import a module in python
# syntax - import module_name
# syntax for importing only few function/variables -> from module_name import f1, f2, f3
# syntax to create an alias for the module that is imported: import module_name as alias_name

# calculate square root of the number
import math
num = 100
output = math.sqrt(num)
print(f"Square root of the {num} is {output}")
print()

# calculate the area of the circle
import math
radius = 2
area_of_circle = math.pi * (radius ** 2)
print(f"The value of pi is {math.pi}")
print(f"Area of the circle with radius {radius} is: {area_of_circle}")
print()

# throw a dice/die
## we need to generate a random value
from random import randint
value = randint(0, 6)
print(f"The random value is: {value}")
print()

# alias
import datetime as dt
print(f"current time {dt.time(hour=23, minute=15, second=35)}")
print(f"current date and time {dt.datetime.now()}")