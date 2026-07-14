"""
marks >= 90 : Grade A
marks 80 and 89 : Grade B
marks 70 and 79 : Grade C
marks 60 and 69 : Grade D
marks < 60 : Grade F
"""

# if-elif-else
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
else:
    print("Grade F")