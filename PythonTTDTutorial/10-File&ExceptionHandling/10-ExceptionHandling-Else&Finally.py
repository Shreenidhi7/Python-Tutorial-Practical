# try:
#     with open("5-File1.txt", "rt") as file_handler:
#         data = file_handler.read()
# except FileNotFoundError as file_error:
#     print("File that you are trying to open does not exist!")
#     print(file_error)
# else:
#     print(data)

import io
try:
    fh = open("10-10-test.txt", "wt")
    fh.write("hello world")
except FileNotFoundError as file_error:
    print("File that you are trying to open does not exist!")
    print(file_error)
except io.UnsupportedOperation as io_error:
    print(io_error)
# else:
#     print("else block")
#     # print(data)
finally:
    print("Finally statement")
    fh.close()