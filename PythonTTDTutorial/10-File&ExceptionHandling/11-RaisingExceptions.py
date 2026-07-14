# raise

# salary = float(input("Enter your salary: "))
#
# if salary < 0:
#     raise ValueError("Your salary cannot be negative")
# else:
#     print(f"Your salary is {salary}")


age = float(input("What is your age = "))
if age < 0:
    raise Exception("Your age cannot be negative")
else:
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("You cannot vote")