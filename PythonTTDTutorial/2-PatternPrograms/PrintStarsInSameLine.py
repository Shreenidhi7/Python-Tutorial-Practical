"""
Print Stars (*'s) in Same Line
n=3 => * * *
n=5 => * * * * *
Take input from the user
"""

numberOfStars = int(input("Enter the n value : "))
# for i in range(1, numberOfStars+1):  # 0,1,2
#     print("*",end=" ")

for i in range(0, numberOfStars):  # 0,1,2
    print("*",end=" ")