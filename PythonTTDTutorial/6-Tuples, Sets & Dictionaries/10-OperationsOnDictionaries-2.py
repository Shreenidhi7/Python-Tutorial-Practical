# not allowed = list, set, dict => mutable data-types
# allowed = str, int, float, bool, tuple => immutable data-types

# keys of a dictionary can only be mutable datatype
# value can be of any datatype

# value = List
student1 = {"id" : 1001, "name": "Shree", "marks" : [89.5, 71.5, 81.0]}
print(student1)
print(student1["name"])
print(student1["marks"][2])

# value = Dictionary
student2 = {"id" : 1001, "name": "Shree", "marks" : {"english" :89.5, "maths" :71.5, "biology" :81.0}}
print(student2)
print(student2["name"])
print(student2["marks"]["english"])

# fetch all the keys of the dictionary
student2 = {"id" : 1001, "name": "Shree", "marks" : {"english" :89.5, "maths" :71.5, "biology" :81.0}}
print(student2)
print(student2.keys(), type(student2.keys()))

# fetch all the values of the dictionary
print(student2)
print(student2.values(), type(student2.values()))

# fetch keys and value both as a pair together
print(student2)
print(student2.items(), type(student2.items()))