"""
Problem Statement -
We have the following dictionary containing details:
user = {
    "user_name" : "my_user",
    "password" : "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 11111",
    "country": "Australia"
}

Delete the sensitive information from the dictionary present in a list
Delete password and address keys from the dictionary
sensitive_info = ["password", "address"]
"""

# user = {
#     "user_name" : "my_user",
#     "password" : "test@123",
#     "email": "my_user@example.com",
#     "address": "ABC road, 11111",
#     "country": "Australia"
# }
# sensitive_info = ["password", "address"]
#
# for i in sensitive_info:
#     print(f"{i} : {user[i]}")
#     user.pop(i)
# print(user)

#################


user = {
    "user_name" : "my_user",
    "password" : "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 11111",
    "country": "Australia"
}
sensitive_info = ["password", "address", "phone"]

for i in sensitive_info:
    if i in user:
        print(f"{i} present in the list \n So Deleting the Key and value from the dictionary => {i} and {user[i]}.")
        user.pop(i)
    else:
        print(f"{i} not present in the list")

print(user)
