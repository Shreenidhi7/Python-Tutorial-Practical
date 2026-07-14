student1 = {"maths" : " 80.5", "english" : " 97.5", "physics" : " 97.5"}

# fetch the key's value using square brackets
# print(f"positive case - using [] brackets : {student1["english"]}")
# print(f"negative case - using [] brackets : {student1["french"]}")

# fetch the key's value using the get() function
print(f"positive case - using get() function : {student1.get('english')}")
print(f"negative case - using get() function : {student1.get('kannada')}")

emp1 = {"id" : 1001, "name" : "John", "salary" : 10000}
print(emp1.get("phone",9876543210))
print(emp1.get("id",111111111111))


print(f"Membership Operators in Dictionaries")
print("id" in emp1)
print("name" in emp1)
print(1001 in emp1)
print("John" in emp1)

print(f"Updating the Dictionary")
sem1_marks = {"marks" : 78.5, "english" : 71.0, "physics" : 86.5}
sem2_marks = {"chemistry": 81.5, "biology": 90.5}
sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {"milk" : 60, "rice" : 100, "biscuits" : 200}
groceries_2 = {"rice" : 110, "bread" : 30}
groceries_1.update(groceries_2)
print(groceries_1)

print(f"Deleting an item from the Dictionary")
groceries_3 = {'milk': 60, 'rice': 110, 'biscuits': 200, 'bread': 30}
print(groceries_3)
groceries_3.pop('milk')
print(groceries_3)

print("Keys duplication Test")
groceries_4 = {'milk': 60, 'rice': 110, 'bread': 30, "milk" : 100}
print(groceries_4)