# Find word in a log file:

with open ("log file.txt") as f:
    content =  f.read().lower()

word = input("Enter the word:")
if word in content:
    print(F"{word} is found in the file")

c = True
i = 1

with open ("log file.txt") as f:
    while c:
        a = f.readline()
        if word in a.lower():
            print(a)
            print(F"{word} is found in the file at line {i}")
        i  += 1