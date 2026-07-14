# filehandler = open("6-Practice1.txt","rt")
# contents = filehandler.read()
# print(contents)
# filehandler.close()

###################

# with open("6-Practice1.txt") as fileHandler:
#     contents = fileHandler.read()
#
# print(contents)

###################

with open("6-Practice2.txt", "xt") as fileHandler:
    fileHandler.write("This file has been created using Python \n")
    fileHandler.write("Bye")