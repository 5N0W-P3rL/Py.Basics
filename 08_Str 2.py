# Make a letter Template:

letter = '''Dear <|NAME|>;
  You're selected.
Date: <|DATE|> \n'''

name = input("Enter recipent's name:\n")
date = input("Enter date:\n")

print("\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)