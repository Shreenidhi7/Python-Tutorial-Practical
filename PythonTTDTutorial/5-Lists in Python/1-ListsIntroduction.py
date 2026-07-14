name = "Shree"
age = 29
percent = 85.5

student = ["Shree", 29, 85.5]
print(student)
print(type(student))

daysOfWeek = ["Mon", "Tue", "Wed", "Thru", "Fri", "Sat", "Sun"]
print(daysOfWeek[0])
print(daysOfWeek[4])

# Positive Indexing
print(f'Last day of the week is {daysOfWeek[6]}')
# Negative Indexing
print(f"Last day of the week is {daysOfWeek[-1]}")

# Length of the List => The number of items/elements in the list
print(f"Length of the list is {len(daysOfWeek)}")

# Index out of range
print(daysOfWeek[8])