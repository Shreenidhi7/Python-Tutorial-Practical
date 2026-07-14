num = int(input("Enter a number: "))

# normal way - traditional way
# if num % 2 == 0:
#     result = "Even"
# else:
#     result = "Odd"
# print(result)

# true-expression : if condition
# false-expression : else condition
# true-expression : if condition else false-expression
print("Even") if num % 2 == 0 else print("Odd")
