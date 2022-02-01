# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
for letter in text.casefold():
    if letter.isalpha():
        word_count[letter] = word_count.setdefault(letter, 0) + 1
    else:
        continue
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
