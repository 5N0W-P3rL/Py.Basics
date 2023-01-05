# Censored words in a file:

word = input("Enter the word:")

with open ("sample.txt") as f:
    a = f.read()

a = a.replace(word, "%$#@#$%")

with open ("sample.txt", "w") as f:
    f.write(a)