# Mutability & Immutability
# Lists are Mutable
# Strings & Tuples are Immutable

# stings
s1 = "Python is Fun"
s2 = s1.replace("Python", "Fun")
print(s1)
print(s2)

# tuples
t1 = ("Mango", "Orange", "Apple")
# t1.append("Banana")
print(t1)

# lists
l1 = ["Mango", "Orange", "Apple"]
print(l1)
print(f"ID of L1 before the change is done : {id(l1)}")
l1.append("Banana")
print(l1)
print(f"ID of L1 after the change is done : {id(l1)}")

# mutability examples with list - possible
l2 = ["Mango", "Orange", "Aple"]
print(l2)
print(f"ID of L2 before the change is done : {id(l2)}")
l2[-1] = "Apple"
print(l2)
print(f"ID of L2 after the change is done : {id(l2)}")

# mutability examples with tuples - not possible
# fruits = ("apple", "banana", "chery")
# print(fruits)
# fruits[-1] = "cherry"
# print(fruits)

# mutability examples with strings - not possible
s2 = "Python is Fun"
print(s2)
s2[0] = "J"
print(s2)