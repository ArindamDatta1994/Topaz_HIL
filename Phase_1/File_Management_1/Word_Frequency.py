import string

file_path = "sample.txt"

with open(file_path, 'r') as file:
    text = file.read()

text = text.upper()

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

word_count = {}

for wrd in words:
    if wrd in word_count:
        word_count[wrd] = word_count[wrd] + 1
    else:
        word_count[wrd] = 1

#print(word_count)

for word, count in word_count.items():
    print(f"{word}: {count}")