# Regular Expression [Regex]

# message = "The current Python version is 3.14"
#
# # Check if "Python", "14" is present in above string
# print("Python" in message)
# print("14" in message)
# print("15" in message)
#
# # Find the index of a character in string
# print(message.find("3.14"))
# print(message.find("Python"))

"""
re.search(regex, string)
=> returns a match object when there is a match found, else returns None
"""

import re
message = "The current Python version is 3.14. Other previous versions are 3.13, 3.12, 3.11."
match_object = re.search("13",message)
print(match_object)

if re.search("13",message):
    print("Found")
else:
    print("Not Found")

# cross-verify
print(message[66:68])