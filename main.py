import string

with open("books/frankenstein.txt") as f:
    text = f.read()

all_characters = {}
alphabet = list(string.ascii_lowercase)

leng_text = len(text.split())

for character in alphabet:
    all_characters[character] = text.lower().count(character)


sorted_dict = dict(reversed(sorted(all_characters.items(), key=lambda item: item[1])))

print("--= Begin report of books/frankenstein.txt ---")
print(f"{leng_text} words found in the document")
for key, value in sorted_dict.items():
    print(f"The '{key}' character was found {value} times")
print("--- End Report ---")

