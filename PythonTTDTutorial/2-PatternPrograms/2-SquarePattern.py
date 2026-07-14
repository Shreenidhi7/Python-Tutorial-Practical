"""
Square Pattern
n = 3
* * *
* * *
* * *
"""

row_size = int(input("Enter the number of rows : "))
# Approach 1
# for i in range(0, row_size):  # if n=3, then its 0,1,2
#     print("* " * row_size)
# print()

# Approach 2
for i in range(0, row_size):    #if n=3, then its 0,1,2
    for j in range( 0, row_size): # if n=3 => i=1, then j=0 & j<3 -> print(*) && then j=1, & j<3 -> print(*) && then j=2 & j<3 -> print(*) && then j=3 & j!<3 (oot of j loop)
        print("*", end=" ")
    print()