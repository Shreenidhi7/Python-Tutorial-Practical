# Sets are non-sequential collection of items
# comma separated elements enclosed within {}

set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# indexing - not allowed in sets
# print(set1[0])

# Length of the set
print(len(set1))

# sets do not allow duplicate elements
l1 = [10,2.5,10,30,10]
print(l1, type(l1))
set1 = {10, 2.5, 10, 30, 10}
print(set1, type(set1))