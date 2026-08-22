def wordFrequencyInASentence(sentence : str) -> dict[str, int]:
    #1. Create an empty dictionary to store our word count
    word_frequency_tracker = {}

    #2. Make the text lowercase, so "Test" and "test" are treated as same word
    lowercase_sentence = sentence.lower()

    #3. Clean out the punctuation marks (dots and commas)
    cleaned_sentence = ""
    for character in lowercase_sentence:
        #Keep regular letters/numbers and spaces skip punctuation marks
        if character.isalpha() or character == " ":
            cleaned_sentence = cleaned_sentence + character

    #4. Split the sentence into a list of individual words
    words_list = cleaned_sentence.split()

    #5. Count each word using our dictionary
    for word in words_list:
        if word in word_frequency_tracker:
            #If the word is already in our dictionary, add 1 to its count
            word_frequency_tracker[word] = word_frequency_tracker[word] + 1
        else:
            #If it's a new word, add it to the dictionary starting at 1
            word_frequency_tracker[word] = 1

    return word_frequency_tracker

text = 'Test the code. Test it again, then test once more.'
total_count = wordFrequencyInASentence(text)

for word, count in total_count.items():
    print(f" {word} : {count}")