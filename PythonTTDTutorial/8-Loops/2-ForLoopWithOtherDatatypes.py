s1 = "Hello World"
print(s1, type(s1))
for char in s1:
    print(char)
print("End of the loop")

t1 = (1,2,4,10,20,30)
print(t1, type(t1))
for num in t1:
    print(num)
print("End of the loop")

employee = { "emp-id" : 1001, "emp-name" : "Shree", "emp-email" : "shree@shrn.in", "emp-department" : "HR" }
print(employee, type(employee))
# to get only the keys
print("To get only the keys")
for i in employee:
    print(i, type(i))
# to get only the values
print("To get only the values")
for i in employee:
    print(employee[i])
# to get keys and values
print("To get keys and values")
for i in employee:
    print(i, employee[i])

# dictionaries items
print(employee.items(), type(employee))
for i in employee.items():
    print(i, type(i))
    print(i[0],i[1])
