file_name = "sample.txt"

with open(file_name, 'r') as file:
    content = file.read()

character_count = len(content)

words = content.split()
word_count = len(words)

lines = content.splitlines()
line_count = len(lines)

print(f"Characters: {character_count}")
print(f"Words: {word_count}")
print(f"Lines: {line_count}")