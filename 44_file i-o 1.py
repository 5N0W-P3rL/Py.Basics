# find a word  in a .txt file 

with open ("sample.txt") as f:
   t =  f.read()

s = input("Enter the word you want to search:")
if s in t:
    print(f"{s} is present in the file.")
else:
    print(f"{s} is not present in the file.")