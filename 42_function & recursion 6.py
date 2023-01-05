# Remove a given word from a string & strip it:

def rmv_n_strip(str, word):
    new_str = str.replace(word, "")
    return new_str
    
str = input("Enter the string:\n")
w = input("Enter the word: ")
new_str = rmv_n_strip(str, w)
print(f"New string is:\n {new_str}")