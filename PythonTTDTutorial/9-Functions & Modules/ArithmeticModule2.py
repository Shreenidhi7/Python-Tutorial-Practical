def add(num1, num2):
    return num1 + num2

def square_root(num):
    return num ** 0.5

print(f"__name__ value in arithmetic module is {__name__}")

if __name__ == "__main__":
    a = 10
    b = 20
    result = add(a, b)
    print(f"Addition of {a} and {b} is {result}")

