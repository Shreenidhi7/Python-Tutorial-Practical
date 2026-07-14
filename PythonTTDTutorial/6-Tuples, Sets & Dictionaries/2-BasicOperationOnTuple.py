# basic operations on tuples
# concatenation, repetition, membership
# count, index
# min, max, sum

# concatenation [+]
print(f"tuple - concatenation operation")
student_details1 = (1001, "Shree")
student_details2 = (78.5, 91.0, 83.5, 79.5)
student_details3 = student_details1 + student_details2
print(f'concatenation of 2 tuple into 1 : {student_details3}')

# repetition [*]
print(f'tuple - repetition operation')
t1 = ("Class 5", 5000)
print(f"repetition of tuple : {t1*3}")

# membership [in,not in]
print(f'tuple - membership operation')
print("student details", student_details3)

print(f" -in-membership")
print(f" is a member: {91.0 in student_details3}")
print(f" is a member: {84.5 in student_details3}")

print(f" -not-in-membership")
print(f" is a member: {92.0 not in student_details3}")
print(f" is a member: {78.5 not in student_details3}")

# count
# tuple.count(element/item)
print(f"tuple - count operation")
t2 = (10,4,1,9,0,3,1)
print(f"count of a element in tuple : {t2.count(1)}")

# index
# tuple.index(element/item)
print(f"tuple - index function/operation")
print(f"find the index of the element/item in the tuple : {t2.index(9)}")
print(f"find the index of the element/item in the tuple : {t2.index(1)}")
# print(f"find the index of the element/item in the tuple : {t2.index(19)}")

# min,max,sum
# min(tuple)
# max(tuple)
# sum(tuple)
print(f"\nmin/max/sum operations")
print(f"minimum value of the tuple : {min(t2)}")
print(f"maximum value of the tuple : {max(t2)}")
print(f"sum of the tuple : {sum(t2)}")