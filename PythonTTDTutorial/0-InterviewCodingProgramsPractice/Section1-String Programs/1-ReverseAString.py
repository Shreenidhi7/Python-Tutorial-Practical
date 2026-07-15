# def reverse_string(s: str) -> str:
#     #1. Convert the string into a list of characters
#     characters = list(s)
#     print(characters)
#
#     #2. Set out starting points on seperate lines
#     left_index = 0
#     right_index = len(characters) - 1
#     print(left_index)
#     print(right_index)
#
#     #3. Start the loop
#     while left_index < right_index:
#         #1. Save the letters in temporary "holding boxes"
#         left_letter = characters[left_index]
#         right_letter = characters[right_index]
#
#         #2. Perform swap using our "holding boxes"
#         characters[left_index] = right_letter
#         characters[right_index] = left_letter
#
#         #3. Move the pointer to the middle, one at a time
#         left_index = left_index + 1
#         right_index = right_index - 1
#
#     #4. Glue it all back together AFTER loop is completely done
#     reversed_string = ''.join(characters)
#     return reversed_string
#
#
# print(reverse_string("racecar"))


###################################################
### Practice
def reverse_string(s: str) -> str:
    #1. Convert the string into a list of characters
    characters = list(s)

    #2. Set the starting points
    left_index = 0
    right_index = len(characters) - 1

    #3. Start the Loop
    while left_index < right_index:
        #1. Save the letters in "hodling boxes"
        left_letter = characters[left_index]
        right_letter = characters[right_index]

        #2. Swap the letter using the holding boxes
        characters[left_index] = right_letter
        characters[right_index] = left_letter

        #3. Move the pointers to the middle
        left_index = left_index + 1
        right_index = right_index - 1

    #4. Return the reversed string
    reversed_string = ''.join(characters)
    return reversed_string

print(reverse_string("racecar"))
print(reverse_string("malayalam"))