filehandler = open("4-practice.txt","rt")

# # read the entire file
# # read operation
# # read() => read the contents of the file as str
# content = filehandler.read()
#
# print(content)
# print(type(content))
#
# # closing a file => close()
# filehandler.close()
#

###############################

# # read the character of the file
# # read operation
# # read() => read the contents of the file as str
# content = filehandler.read(50)
#
# print(content)
# print(type(content))
#
# # closing a file => close()
# filehandler.close()

###############################

# # read the characters/contents of the file - using readline function/method
# # read operation
# # read() => read the contents of the file as str
# line1 = filehandler.readline()
# line2 = filehandler.readline()
# line3 = filehandler.readline()
# line4 = filehandler.readline() #Empty String => the file has reached "End of File" (EOF)
#
# print(f"Line 1: {line1}")
# print(f"Line 2: {line2}")
# print(f"Line 3: {line3}")
# print(f"Line 4: {line4}")
# print(type(line1), type(line2), type(line3), type(line4))

# closing a file => close()
# filehandler.close()

###############################

# # read all the lines together - readlines()
# # read operation
# # read() => read the contents of the file as str
# content = filehandler.readlines()
#
# print(f"Readlines Function Output - {content}")
# print(content[0])
# print(content[1])
# print(content[2])
# print(type(content))
#
# # closing a file => close()
# filehandler.close()

###############################

# read all the lines together - readlines()
# read operation
# read() => read the contents of the file as str
content = filehandler.readlines()

for line in content:
    print(line.rstrip("\n"))

# closing a file => close()
filehandler.close()