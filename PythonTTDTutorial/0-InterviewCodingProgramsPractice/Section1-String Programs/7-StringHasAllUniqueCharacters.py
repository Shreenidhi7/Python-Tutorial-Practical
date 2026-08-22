def all_unique_characters(s: str) -> bool:
    #1. Create an empty collection bag to remember letter we have already seen
    seen_character = set()

    #2. Look for every character in the string, one by one
    for character in s:
        #3. Check if we already dropped this letter/character in the bag
        if character in seen_character:
            return False #Duplicate Found!, Stop immediately and Return False

        #4. If we haven't seen it yet, put it in our bag
        seen_character.add(character)

    #5. If the loop finishes without finding any repeated/duplicate characters,then they all are unique
    return True

print(all_unique_characters("Python"))
print(all_unique_characters("Selenium"))
print(all_unique_characters(""))