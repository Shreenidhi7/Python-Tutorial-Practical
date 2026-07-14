import json

# students = {
#     'student1': { 'roll' : 123, 'name' : 'John', 'percent' : 98.5, 'sports' : True },
#     'student2': { 'roll' : 456, 'name' : 'Mark', 'percent' : 78.5 , 'sports' : False },
#     'student3': { 'roll' : 789, 'name' : 'Mark', 'percent' : 98.5 , 'sports' : True }
# }
# print(students)
# print(type(students))

############################
# # dump
# with open("12-Students.json", "w") as file_handler:
#     json.dump(students, file_handler, indent=4)

#############################
# # load
# with open("12-Students.json", "r") as file_handler:
#     data = json.load(file_handler)
#
# print(data)
# print(type(data))

##############################
# # update
# """
# Read the old data from the existing file
# Update the new data
# """
#
# studentsUpdate = {
#     'student1': { 'roll' : 123, 'name' : 'Shree', 'percent' : 95.5, 'sports' : False },
#     'student2': { 'roll' : 456, 'name' : 'Mark', 'percent' : 78.5 , 'sports' : False },
#     'student3': { 'roll' : 789, 'name' : 'Mark', 'percent' : 98.5 , 'sports' : True }
# }
#
# # read the old data from the json file
# with open('12-Students.json', 'r') as file_handler:
#     data = json.load(file_handler)
#
# # update operation
# data.update(studentsUpdate)
#
# #dump - write the updated data in the json file
# with open('12-Students.json', 'w') as file_handler:
#     json.dump(data, file_handler, indent=4)

########################################

students = {
    'student1': { 'roll' : 123, 'name' : 'John', 'percent' : 98.5, 'sports' : True },
    'student2': { 'roll' : 456, 'name' : 'Mark', 'percent' : 78.5 , 'sports' : False },
    'student3': { 'roll' : 789, 'name' : 'Mark', 'percent' : 98.5 , 'sports' : True }
}

studentsUpdate = {
    'student1': { 'roll' : 123, 'name' : 'Shree', 'percent' : 95.5, 'sports' : False },
    'student2': { 'roll' : 456, 'name' : 'Mark', 'percent' : 78.5 , 'sports' : False },
    'student3': { 'roll' : 789, 'name' : 'Mark', 'percent' : 98.5 , 'sports' : True }
}

try:
    # read the old data from the json file
    with open('12-Students-1.json', 'r') as file_handler:
        data = json.load(file_handler)
except FileNotFoundError:
    with open('12-Students-1.json', 'w') as file_handler:
        json.dump(students, file_handler, indent=4)
else:
    # update operation
    data.update(studentsUpdate)

    #dump - write the updated data in the json file
    with open('12-Students-1.json', 'w') as file_handler:
        json.dump(students, file_handler, indent=4)