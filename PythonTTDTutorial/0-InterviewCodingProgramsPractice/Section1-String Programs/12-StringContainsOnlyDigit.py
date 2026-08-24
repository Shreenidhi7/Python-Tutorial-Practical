def is_all_digits(s: str) -> bool:
    #1. Edge Case - An Empty String doesn't contain any digits
    if len(s) == 0:
        return False

    #2. Check every character in the string one by one
    for character in s:

        # If a character is not Digit (Like '.'. spaces, letters etc.) -> return False
        if not character.isdigit():
            return False

    # 4. If the loop finishes without finding any non-digit characters, return True!
    return True

print(is_all_digits("12345")) # Output: True
print(is_all_digits("3.14")) # Output: False (because of the decimal point '.')
print(is_all_digits(" "))  # Output: False (because it is empty space)
print(is_all_digits("")) # Output: False (because it is empty)
print(is_all_digits('²'))  # Output: True (Python recognizes '²' as a numeric digit)