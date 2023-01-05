# wipe out a file:

file = input("Enter the file name: ")
with open (f"{file}.txt", "w") as f:
    f.write("")