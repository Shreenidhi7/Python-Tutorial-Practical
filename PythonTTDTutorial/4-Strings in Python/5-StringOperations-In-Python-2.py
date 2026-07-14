# Counting the characters/substring from a string
print("Counting the characters/substring from a string")
s1 = "We are learning Python. Python is fun"
s2 = "Python"
s3 = "e"
s4 = "learn"
s5 = " "
print(s1.count(s2))
print(f"Occurrences of {s2} is {s1.count(s2)}")

print(s1.count(s3))
print(f"Occurrences of {s3} is {s1.count(s3)}")

print(s1.count(s4))
print(f"Occurrences of {s4} is {s1.count(s4)}")

print(s1.count(s5))
print(f"Occurrences of empty-spaces is {s1.count(s5)}")

#########################################
# Changing case of a string
print("Changing case of a string ")

a1 = "Python3.14"
print(a1.upper())
print(a1.lower())

a2 = "We are learning Python. Python is fun"
print(a2.upper())
print(a2.lower())

a3 = "We are learning Python again and again"
print(a3.title())

a4 = "We are learning Python again and again. Python is REALLY FUN!!"
print(a4.capitalize())

##############################################
# Starting and Ending of a string
print("Starting and Ending of a string")

b1 = "We are learning Python"
print(b1.startswith("We are"))
print(b1.startswith("we"))

print(b1.endswith("Python"))
print(b1.endswith("n"))
print(b1.endswith("Pytho"))