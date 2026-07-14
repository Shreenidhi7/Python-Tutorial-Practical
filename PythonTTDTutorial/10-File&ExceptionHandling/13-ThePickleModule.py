# students = {
#     'student1': {'roll': 101, 'name' : 'John', 'percent' : 78.5},
#     'student2': {'roll': 102, 'name' : 'Michael', 'percent' : 97.5},
#     'student3': {'roll': 103, 'name' : 'Michael', 'percent' : 97.5},
# }
#
# print(students)
# print(type(students))
#
# # with open('13-StudentsInfo.txt', 'wt') as file_handler:
# #     file_handler.write(students)
#
# with open('13-StudentsInfo.txt', 'rt') as file_handler:
#     content = file_handler.read()
#
# print(type(content))
# output = dict(content)
# print(output)


import pickle

students = {
    'student1': {'roll': 101, 'name' : 'John', 'percent' : 78.5},
    'student2': {'roll': 102, 'name' : 'Michael', 'percent' : 97.5},
    'student3': {'roll': 103, 'name' : 'Michael', 'percent' : 97.5},
}

print(students)
print(type(students))

# Serialization
with open('13-students.bin', 'bw') as file_handler:
    for student in students:
        pickle.dump(students[student], file_handler)

# De-Serialization
with open('13-students.bin', 'rb') as file_handler:
    data1 = pickle.load(file_handler)
    print(data1, type(data1))
    data2 = pickle.load(file_handler)
    print(data2, type(data2))
    data3 = pickle.load(file_handler)
    print(data3, type(data3))