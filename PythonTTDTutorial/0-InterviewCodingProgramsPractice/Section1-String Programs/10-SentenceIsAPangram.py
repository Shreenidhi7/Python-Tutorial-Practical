def sentence_is_pangram(sentence: str) -> bool:
    #1. Define all 26 alphabets of english language
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    #2. Make the sentence lowercase, so the capital letters match easily\
    lowercase_sentence = sentence.lower()

    #3. Check every single letter of the alphabet one by one
    for letter in alphabets:

        #If any particular alphabet letter is missing from the sentence, then the sentence is not a Pangram
        if letter not in lowercase_sentence:
            return False

    #4. If the loop finishes and found every single letter, then it's a Pangram
    return True

print(sentence_is_pangram('The quick brown fox jumps over the lazy dog')) # Output: True
print(sentence_is_pangram('Hello world'))                                # Output: False
print(sentence_is_pangram('Pack my box with five dozen liquor jugs')) #Output: True