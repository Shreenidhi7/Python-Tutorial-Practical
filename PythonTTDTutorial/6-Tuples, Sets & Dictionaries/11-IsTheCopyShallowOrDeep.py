import copy

# # shallow copy
# # list
# l1 = [1, 2.5, [10,20,30], "Python"]
# print("l1 -",l1)
# print("memory address of l1", id(l1))
# l2 = copy.copy(l1)
# print("l2 -",l2)
# print("memory address of l2", id(l2))
# l1[0] = 5
# l1[2][0] = 50
# print(f"l1 -> {l1}", id(l1))
# print(f"l2 -> {l2}", id(l2))

# # deep copy
# # list
# l1 = [1, 2.5, [10,20,30], "Python"]
# print("l1 -",l1)
# print("memory address of l1", id(l1))
# l2 = copy.deepcopy(l1)
# print("l2 -",l2)
# print("memory address of l2", id(l2))
# l1[0] = 5
# l1[2][0] = 50
# print(f"l1 -> {l1}", id(l1))
# print(f"l2 -> {l2}", id(l2))

#########################################
# dictionary

# shallow copy
d1 = {"id" : 1111, "name" : "John", "marks": {"eng": 71.5, "maths" : 91.5, "bio" : 80.0}}
print("d1",d1)
d2 = copy.copy(d1)
print("d2",d2)
d1["name"] = "Dan"
d1["marks"]["maths"] = 92.5
print(f"d1 {d1}", id(d1))
print(f"d2 {d2}", id(d2))

# # deep copy
# d1 = {"id" : 1111, "name" : "John", "marks": {"eng": 71.5, "maths" : 91.5, "bio" : 80.0}}
# print("d1",d1)
# d2 = copy.deepcopy(d1)
# print("d2",d2)
# d1["name"] = "Dan"
# d1["marks"]["maths"] = 92.5
# print(f"d1 {d1}", id(d1))
# print(f"d2 {d2}", id(d2))