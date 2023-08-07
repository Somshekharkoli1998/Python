input_sequence = input("Enter a sequence of whitespace-separated words: ")
words_list = input_sequence.split()

unique_words = sorted(set(words_list))

print(' '.join(unique_words))
