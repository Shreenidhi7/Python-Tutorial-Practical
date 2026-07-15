def isAPalindrome(s: str) -> bool:
    #1. Step 1 - Clean the text
    # We want to ignore spaces, captial letter, punctuations
    cleaned_letters = []

    for characters in s:
        # Check if the characters are letters and numbers [alphanumeric]
        if characters.isalnum():
            lowercase_characters = characters.lower()
            cleaned_letters.append(lowercase_characters)

    #2. Step2 - Match the characters/letters
    # Set the pointers
    left_index = 0
    right_index = len(cleaned_letters) - 1

    # Start the loop
    while left_index < right_index:
        # Save the letters in the holding boxes
        left_letter = cleaned_letters[left_index]
        right_letter = cleaned_letters[right_index]

        # Check if the characters of the string is a palindrome or not
        # If the letters don't match, it's not a palindrome
        if left_letter != right_letter:
            return False

        # Move the pointers to the center/middle
        left_index = left_index + 1
        right_index = right_index - 1

    # If the loop finishes without finding any mismatched letters, then its a palindrome
    return True

print(isAPalindrome("racecar"))
print(isAPalindrome("malayalam"))
print(isAPalindrome("s"))
print(isAPalindrome("shree"))