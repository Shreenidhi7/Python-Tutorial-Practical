# os.path.exists()

import os
# file_name = "7-Practice.txt"
# if os.path.exists(file_name):
#     print("File Exists")
# else:
#     print("File Does Not Exist")

# file_name = "D:/Python/PythonTTDTutorial/10-File&ExceptionHandling/7-Practice.txt"
# if os.path.exists(file_name):
#     print("File Exists")
# else:
#     print("File Does Not Exist")


#########################################

# from pathlib import Path
# file_name = Path("D:/Python/PythonTTDTutorial/10-File&ExceptionHandling/7-Practice.txt")
# if file_name.exists():
#     print("File Exists")
# else:
#     print("File Not Exists")

from pathlib import Path
file_name = Path("D:/Python/PythonTTDTutorial/10-File&ExceptionHandling/7-Practice1.txt")
if file_name.exists():
    print("File Exists. Cannot Create")
else:
    print("File Doesnot Exists, Creating It")
    file_handler = open(file_name, "xt")
    file_handler.write("new content")
    file_handler.close()