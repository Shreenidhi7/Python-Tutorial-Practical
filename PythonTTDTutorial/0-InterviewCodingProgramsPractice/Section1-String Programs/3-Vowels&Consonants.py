# def count_vowels_consonants(s: str) -> tuple[int, int]:
#     #1. Setup out vowel tracker and counter on seperate lines
#     vowel_letters = "aeiou"
#     vowels_count = 0
#     consonant_count = 0
#
#     #2. Make the entire text lower case, so we don't have to worry about capital letters
#     lowercase_text = s.lower()
#
#     #3. Look for every character one by one
#     for characters in lowercase_text:
#         # Check if the letters are regular letters [A-Z]
#         if characters.isalpha():
#             # If its a letter, check if that letter lives inside out vowel string
#             if characters in vowel_letters:
#                 vowels_count = vowels_count + 1
#             else:
#                 # If it's a letter but NOT a vowel, it must be a consonant!
#                 consonant_count = consonant_count + 1
#
#         # If its a number or a space, the code simply ingnores it and moves on
#
#     #4. Return both final counts back as a package
#     return vowels_count, consonant_count
#
#
# result = count_vowels_consonants("Selenium Webdriver 4")
# # Unpack the package into two separate variables
# final_vowel_count = result[0]
# final_consonant_count = result[1]
# print(f"final vowel count : {final_vowel_count}")
# print(f"final consonant count : {final_consonant_count}")

def count_vowels_consonants(s: str) -> tuple[int, int]:
    #1.Set up out vowel tracker and counters
    vowel_letters = "aeiou"
    vowel_count = 0
    consonant_count = 0

    #2.Make sure the entire text is lowercase(so that we don't have to worry about capital letters)
    lowercase_letters = s.lower()

    #3.Look for every character one by one
    for character in lowercase_letters:
        #Check if the characters are alphabets
        if character.isalpha():

            #Check if the character/letter live under vowel string which we have declared
            if character in vowel_letters:
                vowel_count = vowel_count + 1
            else:
                #If a letter is not a vowel, then it should be a consonant
                consonant_count = consonant_count + 1

        #If it's a number or space, then code will simply ignore it and move on
    return vowel_count, consonant_count

result = count_vowels_consonants("Selenium Webdriver 4")
vowelCount = result[0]
consonantCount = result[1]
print(f"{vowelCount} : {consonantCount}")