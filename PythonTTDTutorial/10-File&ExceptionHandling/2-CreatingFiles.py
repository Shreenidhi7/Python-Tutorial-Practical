# # create a file - x mode
# # if the file doesn't exist, it will create a file.
# fh = open("2-file1.txt", "xt")
#
# # writing into a file
# # write(content)
# fh.write("This file is created using the 'x' mode in Python \n Second line" )
# fh.write("\nThird line")
#
# # closing the file
# fh.close()
from os import write

#########################
##### ERROR

# create a file - x mode
# if the file doesn't exist, it will create a file.
fh = open("2-file1.txt", "xt")

# writing into a file
# write(content)
fh.write("This file is created using the 'x' mode in Python \n Second line" )
fh.write("\nThird line")

# closing the file
fh.close()

# write after closing the file will result in error
fh = write("Write after closing the file")