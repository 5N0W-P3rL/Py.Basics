# rename a file:

import os

file_o = input("Enter the old file name: ")
file_n = input("Enter the new file name: ")

with open (f"{file_o}", "r") as f:
    a = f.read()

with open (f"{file_n}", "w") as f:
    f.write(a)

os.remove(f"{file_o}")