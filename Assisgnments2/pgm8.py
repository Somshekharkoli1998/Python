input_sequence = input("Enter a comma-separated sequence of words: ")
words_list = input_sequence.split(',')
sorted_words = sorted(words_list)

sorted_sequence = ','.join(sorted_words)
print(sorted_sequence)
