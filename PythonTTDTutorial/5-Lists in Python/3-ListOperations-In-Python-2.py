# extend
# remove
# pop

# extend
print("extend function")

fruits = ["apple", "banana", "cherry"]
print(f"the total number of fruits before the extend function is : {len(fruits)} and the fruits are {fruits}")
fruits.extend(["orange","mango"])
print(f"the total number of fruits after the extend function is : {len(fruits)} and the fruits are {fruits}")


# # extend with multiple values
# fruits.extend("tomato", "pineapple")
# print(fruits)

# append with multiple values but in an array
fruits.append(["tomato","pineapple"])
print(fruits)
print(len(fruits))

# fruits.extend(["tomato","pineapple"])
# print(fruits)
# print(len(fruits))

# Remove Function
print(f"Remove Function")

fruitsAgain = ["Apple", "Mango", "Orange"]
print(f"List of fruits before the remove function is : {fruitsAgain} and the length is {len(fruitsAgain)}")

fruitsAgain.remove("Orange")
print(f"List of fruits after the remove function is : {fruitsAgain} and the length is {len(fruitsAgain)}")

# fruitsAgain.remove("Pineapple")
# print(f"List of fruits after the remove function is : {fruitsAgain} and the length is {len(fruitsAgain)}")

fruitsAgainAndAgain = ["Apple", "Mango", "Orange", "Mango"]
print(f"List of fruits before the remove function is : {fruitsAgainAndAgain} and the length is {len(fruitsAgainAndAgain)}")

fruitsAgainAndAgain.remove("Mango")
print(f"List of fruits after the remove function is : {fruitsAgainAndAgain} and the length is {len(fruitsAgainAndAgain)}")

# Pop Function
print("\nPop Function")
fruitsPop = ["apple", "banana", "cherry"]
print(fruitsPop)
fruitsPop.pop(1)
print(fruitsPop)

fruitsPop2 = ["apple", "banana", "cherry", "mango"]
print(fruitsPop2)
fruitsPop2.pop(-1)
print(fruitsPop2)

fruitsPop3 = ["apple", "banana", "cherry"]
print(fruitsPop3)
fruitsPop3.pop()
print(fruitsPop3)
