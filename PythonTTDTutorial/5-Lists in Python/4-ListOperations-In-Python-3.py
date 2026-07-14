'''
List Operations -3
reverse()
sort()
count()
Membership Operation
'''
import numbers

# reverse function [reverse()]
print("\nReverse Function")
days_Of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print("days_Of_week - before reverse", days_Of_week)
days_Of_week.reverse()
print("days_Of_week - after reverse", days_Of_week)

# sort function [sort()]
print("\nSort Function")
nums = [4,9,0, 1,2, 8]
print("nums - before sort", nums)
nums.sort()
print("nums - after sort - ascending", nums)
# nums.reverse()
# print("nums - after reverse", nums)
nums.sort(reverse=True)
print("nums - after sort - reverse/descending", nums)


# count function [count()]
print("\nCount Function")
numbers = [ 0, 1, 3, 4 , 1, 0, 5, 0, 0, 3, 0]
print(f"The list is : {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
count = numbers.count(item_to_count)
print(f"The Occurrence of {item_to_count} is {count} times")

language = ["Python", "Java", "C++", "Python"]
print(f"\nThe list is : {language}")
item_to_count_langugage = input("Enter the language to be counted from the above list: ")
count_language = language.count(item_to_count_langugage)
print(f"The Occurrence of {item_to_count_langugage} is {count} times")

# membership operation [ in ] and [ not in ]
language_in = ["Python", "Java", "C++", "Python"]
print(f"\nThe list is : {language_in}")
print("'in operation'")
print("Python" in language_in)
print("Javascript" in language_in)

print("'not in' operation")
print("C++" not in language_in)
print("JavaScript" not in language_in)