# def are_anagrams(first_word: str, second_word: str) -> bool:
#     #1. Clean the 1st word
#     # Remove spaces and convert everything to lowercase
#     clean_first = first_word.replace(" ", "")
#     lower_first = clean_first.lower()
#
#     #2. Clean the 2nd word
#     # Remove spaces and convert everything to lowercase
#     clean_second = second_word.replace(" ", "")
#     lower_second = clean_second.lower()
#
#     #3. Quick Length Check
#     # If the lenghts are different, they can't be possibly anagrams
#     if len(lower_first) != len(lower_second):
#         return False
#
#     #4. Sort the letters
#     # Organize the letters in both words alphabetically(A-Z)
#     sorted_first = sorted(lower_first)
#     sorted_second = sorted(lower_second)
#
#     #5. Compare the sorted list
#     # If the sorted lists are identical, they are anagrams
#     if sorted_first == sorted_second:
#         return True
#     else:
#         return False
#
#
# print(are_anagrams("listen", "silent"))
# print(are_anagrams("Dormitory", "Dirty Room"))
# print(are_anagrams("Hello", "World"))

###################################################
### Practice

def are_anagrams(first_word : str, second_word : str) -> bool:
    #Step-1: Clean up the first word
    ## Remove spaces and convert everything to lowercase
    clean_first = first_word.replace(" ", "")
    lower_first = clean_first.lower()

    #Step-2: Clean up the second word
    ## Remove spaces and convert everything to lowercase
    clean_second = second_word.replace(" ", "")
    lower_second = clean_second.lower()

    #Step-3: Quick Length Check
    ##If the length of first and second word is not same, then they cannot be anagrams
    if len(lower_first) != len(lower_second):
        return False

    #Step-4: Sort the letters
    ## Organize the letters in both words alphabetically(A-Z)
    sorted_first = sorted(lower_first)
    sorted_second = sorted(lower_second)

    #Step-5: Compare the sorted list
    ## If the sorted lists are identical, then they are anagrams
    if sorted_first == sorted_second:
        return True
    else:
        return False

print(are_anagrams("silent", "listen"))
print(are_anagrams("dirty room", "dormitory"))
print(are_anagrams("hello", "world"))