# Tuple
# (item1, item2, ...)
# sequence of items as a collection
from typing import List

t1 = ("Python", 10, 1.5, True, [1,2,4], (10,20))
print(t1)
print(type(t1))
# length of the tuple
print(len(t1))
# accessing the items of the tuple - index
print(t1[0])
print(t1[-1])
# slicing the items of the tuple
print(t1[1:5:1])

##################
# another way to create a tuple
t2 = 10,20,30,40,50
print(t2)
print(type(t2))

###############
# converting list to a tuple
l3 = [10,20,30,40,50]
print(l3)
print(type(l3))
t3 = tuple(l3)
print(t3)
print(type(t3))

#####################
# converting tuple to a list
fruits = ("mango", "orange", "apple", "banana")
print(fruits, type(fruits))

fruitsList = list(fruits)
print(fruitsList, type(fruitsList))