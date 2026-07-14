# **kwargs - variable length keyword arguments (o to m)
#
# def func(**kwargs):
#     print(kwargs, type(kwargs))
#
# func(x=10, y=20)

# # empty dictionary without any arguments passed
# def func(**kwargs):
#     print(kwargs, type(kwargs))
#
# func()


# def student_details(sid, sname, **marks):
#     if len(marks) == 0:
#         print(f"{sname} did not attend the exam")
#     else:
#         present = sum(marks.values()) / len(marks)
#         print(f"{sname} with id {sid} secured {present}%")
#
# student_details(101, "Shree", sub1 = 78.95, sub2 = 81.00, sub3 = 93.72)
# student_details(201, "Nidhi", sub4 = 73.33, sub5 = 86.66, sub6 = 99.99, sub7 = 60.00)

def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:
        present = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {present}%")
    print(f"{sname} does {extra} time")

student_details(101, "Shree", "Footbal" , sub1 = 78.95, sub2 = 81.00, sub3 = 93.72)
student_details(201, "Nidhi", "Cricket", "Hockey" ,sub4 = 73.33, sub5 = 86.66, sub6 = 99.99, sub7 = 60.00)

