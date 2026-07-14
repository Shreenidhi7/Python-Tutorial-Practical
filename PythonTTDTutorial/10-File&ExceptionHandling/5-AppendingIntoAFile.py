# 'a' mode => append mode

# file_handler = open("5-File1.txt", 'a+t' )
# file_handler.write("\n This content has been written using 'a' mode \n")
# file_handler.write("'a' mode is used to add new content at the end of the file \n")
# file_handler.write("Good Bye!")
# file_handler.close()

file_handler = open("5-File2.txt", 'a+t' )
file_handler.write("This content has been created using 'a' mode \n")
file_handler.write("'a' mode creates a file, if the file doesn't exist \n")
file_handler.write("Good Bye!")
file_handler.close()