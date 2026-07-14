s1 = "Python is fun"

# First character of the string
print(s1[0])

# Last character of the string
print(s1[-1])

# Length of the string
print(len(s1))

# String Concatenation [Plus operator acts as a concatenation operator]
language = "Python"
version = "3.13.3"
print(language+version)

# String Repetition [Multiplication]
print(language*3)

###############################

# Membership operation

# in
print("in - membership operator")
s1 = "Python is fun"
# Expect True
print("Python" in s1)
print("i"in s1)
# Expect False
print("z"in s1)
print("Java" in s1)

# not in
print("not in - membership operator")
s1 = "Python is fun"
# Expect False
print("Python" not in s1)
print("i" not in s1)
# Expect True
print("z" not in s1)
print("Java" not in s1)

###################
# Comparison operator
print("Comparison Operators - Equality")
print("Python" == "Python")
print("Python " == "Python")

####################
# Removing spaces form a string - strip()
print("Strip Function")
s1 = "Python "
s2 = s1.strip()
print(s1)
print(s2)

###################
# Replace a String or a part of the String [replace()]
print("Replace String")
s1 = "We are learning Python"
print(s1)
print(s1.replace("Python","Java"))

print(s1.replace("e","E"))
print(s1)

print(s1.replace("e","E",count=1))
print(s1)
