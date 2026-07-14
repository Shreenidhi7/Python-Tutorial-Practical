# w mode - open the file for writing.
## Its overwrites the file

# fh = open("3-file2.txt", "wt")
# fh.write("This file is overwritten using 'w' mode in Python - New Content\n")
# fh.write("Have a nice day!, New Content")
# fh.close()

fh = open("3-file3.txt", "wt")
fh.write("This file is overwritten using 'w' mode in Python \n")
fh.write("Have a nice day!,")
fh.close()