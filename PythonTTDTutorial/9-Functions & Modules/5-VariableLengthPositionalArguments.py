# *args - variable length positional arguments (o to m)
# def add(*args):
#     print(args, type(args))
#
# add(10,20,30,40,50)

# def add(*args):
#     print(args, type(args))
#     return sum(args)
#
# result = add(10,20,30,40,50)
# print(result)

# def add(*args):
#     print(args, type(args))
#     return sum(args)
#
# result = add()
# print(result)

# def add(*nums):
#     print(nums, type(nums))
#     return sum(nums)
#
# result = add(10,20)
# print(result)

def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in all the exams")
    else:
        percent = sum(marks)/len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(101, "Shree", 20, 30, 40, 50)
student_details(201, "Nidhi", 30, 40, 50, 60, 70, 80)
student_details(301, "Sharma", 40, 50)
student_details(401, "Nag")