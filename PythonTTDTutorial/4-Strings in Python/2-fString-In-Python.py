name = "Shree"
age = 29
language = "Python"
hours = 3

# Shree is 29 years old
print(name,"is",age,"years old")

# Shree is 29 years old. He studies Python 3 hours a day
print(name,"is",age,"years old. He studies",language,hours,"a day")

# Using fString
print(f"{name} is {age} years old. He studies {language} {hours} a day")

sub1 = 78
sub2 = 87
sub3 = 83
total = sub1 + sub2 + sub3
print(f"{name} scored {total} marks in total")
print(f"{name} scored {sub1+sub2+sub3} marks in total")

percent = (sub1 + sub2 + sub3)/100
#Without fString
print("{name} scored {percent:.2f}% in total")

#With fString
print(f"{name} scored {percent:.2f}% in total")
