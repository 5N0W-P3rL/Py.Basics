# Detect double spaces in a string & replace them with single space:

str = input("Enter Your string:\n")
print("\n")
print("Number of double speces in your string:",str.count("  "))
print("\n")
print("New string after replacing double spaces with single spaces:\n",str.replace("  "," "))