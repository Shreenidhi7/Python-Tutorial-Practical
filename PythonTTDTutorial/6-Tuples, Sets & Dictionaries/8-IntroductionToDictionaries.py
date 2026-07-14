# comma separated key value pairs enclosed within curly brackets
# syntax = {key1:value1, key2: value2, ...}

groceries = {"milk":60, "biscuits":20, "rice": 90, "bread": 30}
print(groceries, type(groceries))
# print(len(groceries))
#print(groceries["milk"])
# groceries["milk"] = 65
# print(groceries, type(groceries))

# print(groceries["eggs"])

groceries["eggs"] = 10 # adds new key-value pair to the dictionary
print(groceries, type(groceries))
groceries["bread"] = 50 # updates the value of the key
print(groceries, type(groceries))