def first_unique_character(s: str) -> str | None :
    #1. Loop through every character in a string - one by one
    for character in s:
        #2. Check how many times the specific character appears in the string
        occurrence_count = s.count(character)

        #3. As we find a character with the count of 1, return it immediately
        if occurrence_count == 1:
            return character

    #4. If the loop finishes without finding any single-count letter, return None
    return None

print(first_unique_character("aab"))
print(first_unique_character("swiss"))
print(first_unique_character("aabbcc"))
print(first_unique_character("aabbccd"))