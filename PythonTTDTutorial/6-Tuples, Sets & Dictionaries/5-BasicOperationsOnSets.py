nums = {1, 3, 2 , 0, -1}

# membership operator - in and not in
print(f"membership operators - in and not in")

print(0 in nums)
print(10 not in nums)

print(5 in nums)
print(1 not in nums)

# concatenation operation - not possible on sets
print(f"Concatnation Operation on Sets - Not Possible")
num1 = {1, 2, 3}
num2 = {4, 5, 6}
# print(num1 + num2)

# repetition operation - not possible on sets
print(f"Repetition Operation on Sets - Not Possible")
# print(num1 * 3)

# converting tuple to set
print(f"Converting Type to Sets")
weekdays = ("mon", "tue", "wed", "thur", "fri", "sat", "sun")
weekdays_set = set(weekdays)
print(weekdays_set, type(weekdays_set))

# Are Sets Mutable or Immutable?
print(f"\nAre Sets Mutable or Immutable?")
set1 = {2, 0, -1}
print(f"Before the add function : {set1} and the type of the variable is : {type(set1)}")
# add()
set1.add(5)
print(f"After the add function : {set1} and the type of the variable is : {type(set1)}")
# remove()
set1.remove(5)
print(f"After the remove function : {set1} and the type of the variable is : {type(set1)}")
# set1.remove(5)
# print(f"After the remove function : {set1} and the type of the variable is : {type(set1)}")

# add again()
print(f"set1 : {set1}")
set1.add(2)
print(f"set1 after adding 2 : {set1}")

# discard()
print(f"set1 : {set1}")
set1.discard(2)
print(f"set1 after discarding : {set1}")
set1.discard(10)
print(f"set1 after discarding the element not present in set : {set1}")
