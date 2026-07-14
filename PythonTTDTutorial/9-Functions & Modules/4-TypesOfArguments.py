# # Positional Argument - Passing the arguments in order of their position
# def add(a, b):
#     return a + b
# result = add(1)
# print(result)

# # Default Argument
# def add(a, b=10):
#     print(f"a : {a}, b : {b}")
#     return a + b
# # result = add(1,2)
# # print(result)
# result = add(1)
# print(result)

# def add(a, b, c=10):
#     print(f"a: {a} , b: {b} , c: {c}")
#     return a + b + c
#
# result = add(10, 20, 30)
# print(result)
#
# result1 = add(10, 20)
# print(result1)

# Keyword/Named Argument
def add(a, b=10, c=10):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c

result = add(10,c=50)
print(result)