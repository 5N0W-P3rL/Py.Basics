# Find out whether two files are identical or not:

with open ("sample.txt") as f:
    a = f.read()

with open ("copy_sample.txt") as f:
    b = f.read()

if a == b:
    print("Both files are identical.")
else:
    print("Both files are not identical.")