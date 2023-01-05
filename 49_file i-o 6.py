# copy a text file:

with open ("sample.txt") as f:
    c = f.read()

with open ("copy_sample.txt", "w") as f:
    f.write(c)

print("You copy the file successfully.")