def longest_word_in_a_sentence(sentence : str) -> str:
    #1. Split sentence into a list of separate words
    words = sentence.split()

    #2. Setup variable to track our winning word and its length
    longest_word = ""
    max_length = 0

    #3. Check each word in the list one by one
    for word in words:
        current_word_length = len(word)

        #If this word is longer than the previous record, update the winner
        if current_word_length > max_length:
            longest_word = word
            max_length = current_word_length

    #4. Return the longest word found(Or empty string
    return  longest_word

print(longest_word_in_a_sentence("Automation testing saves time"));
print(longest_word_in_a_sentence("My name is Shreenidhi"))
