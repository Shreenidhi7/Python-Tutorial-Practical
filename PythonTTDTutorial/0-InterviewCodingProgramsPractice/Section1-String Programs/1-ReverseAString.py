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
    #1. Turn the strings into a list of character blocks
    character = list(s)

    #2. Set up our starting points(positions)
    left_index = 0
    right_index = len(character) - 1

    #3. Start the loop
    while left_index < right_index:
        #Save letters in temporary holding boxes, so that we don't lose them
        left_letter = character[left_index]
        right_letter = character[right_index]

        #Perform Swap using our holding boxes
        character[left_index] = right_letter
        character[right_index] = left_letter

        #Move the pointers(positions) to the middle, one at a time
        left_index = left_index + 1
        right_index = right_index -1

    #4. Glue it all back together "After" the loop is completely done
    reversed_string = "".join(character)
    return reversed_string

print(reverse_string("automation"))
print(reverse_string("racecar"))