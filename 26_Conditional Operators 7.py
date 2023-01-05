# Find a tagged person in a post:

person = input("Enter the person's name; about whom you want to search: \n")
post = input("Enter the post:")

if (person in post):
    print(person + " is mentioned in the post.")
else:
    print(person + " is not mentioned in the post.")

# --> How to find the person's name in any format ie.[Sam, SAM, sAm, SaM, #sam etc.] in the post