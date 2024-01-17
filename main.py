with open("books/frankenstein.txt") as f:
    text = f.read()

num_words = len(text.split())
print(num_words)