# range() - built-in function in python.
# It is used to generate a sequence of integers

# Range - 1
# for i in range(start,stop,step):
    #statements1

# even numbers from 1 to 10 [exclude 10]
# for i in range(2, 10,2):
#     print(i)

# generate numbers in the reverse order : 20 to 10 (excluding 10) - only even numbers
# for i in range(20,10,-2):
#     print(i)

# # countdown from 10 to 1 ( 1 included)
# for i in range(10,0,-1):
#     print(i)
# print("Happy New Year")

######################################
# Range - 2
# for i in range(start, stop):
#     statements1
# for i in range(1,5):
#     print(i)

######################################
# Range - 3
# range(stop) = > 0 to stop - 1 with a step 1, start = 0 by default
# start = 0, step = 1 => 0,1,2,3,4
# for i in range(5):
#     print(i)

########################################
# - We shall look at the use case specifically with the sequences on how we can use it.
# we shall print the indexes of the list groceries
# groceries = ["salt","milk","sugar"]
# for index in range(len(groceries)):
#     print(index)

###########
# profit of quarter 1 -
# profit of quarter 2 -
# profit of quarter 3 -
# profit of quarter 4 -

profits = [9, 11, 6, 10]
for index in range(len(profits)):
    quarter = index + 1
    print(f"profit of quater {quarter} - {profits[index]}")