# Opening a file in Python

# open(file_name, mode_to_open)
# mode - r(read), x(create), w(write), a(append), t(text), b(binary)
# if we don't give also -> 'rt' will be the default mode

file_handler = open("1-practice.txt", "rt")
print(file_handler)
#read operation

#close a file  => close()
file_handler.close()