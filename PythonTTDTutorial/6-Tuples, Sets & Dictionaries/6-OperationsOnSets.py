student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}
print(f"subjects of student1 : {student1}, and type of student1 : {type(student1)}")
print(f"subjects of student2 : {student2}, and type of student2 : {type(student2)}")

# INTERSECTION
# common subjects of student1 and student2
# common_subjects = student1.intersection(student2)
common_subjects = student1 & student2 & student3
print(f"common subjects of student1 and student2 : {common_subjects} and type of common_subjects : {type(common_subjects)}")

# common_subjects_again = student1.intersection(student2, student3)
common_subjects_again = student1 | student2 | student3
print(f"common subjects of student1, student2 and student3 : {common_subjects} and type of common_subjects : {type(common_subjects)}")

# UNION
# all subjects of student1 and student2
all_subjects = student1.union(student2, student3)
all_subjects_again = student1 | student2 | student3
print(f"all subjects of student1 and student2 and student3 : {all_subjects} and type of all_subjects : {type(all_subjects)}")

# DIFFERENCE
days = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

weekdays = days.difference(weekends)
weekdays_again =  days - weekends
print(f"weekdays : {weekdays}")