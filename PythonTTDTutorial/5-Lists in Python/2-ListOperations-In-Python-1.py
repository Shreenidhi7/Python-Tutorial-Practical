# Slicing of 5-Lists in Python
print("Slicing of Lists")
l1 = [3,8,1,0,4,9,7,3,6]
print(len(l1))
print(l1[1:6:1])
print(l1[2:7:2])

# Concatenation of 5-Lists in Python
print("\nConcatenation of Lists")

l2 = [ 1, 7, 2]
l3 = [0, 5]
print(l2 + l3)
print(l3 + l2)

# Repetition of 5-Lists in Python
print("\nRepetition of Lists")
print(l3 * 3)

# Functions in List
# Append Function
print("\nAppend Function")
fruits = ["mango", "apple", "orange"]
print(fruits)
fruits.append("banana")
print(fruits)

# insert function
## adds an element before the specified index
# syntax = list.insert(index,item)
print("\nInsert Function")
print(f"Before Inserting Function {fruits}")
fruits.insert(2, "cherry")
print(f"After Inserting Function {fruits}")