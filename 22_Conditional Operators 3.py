# Finding spam Comments:

c1 = "Make lot of money"
c2 = "Buy now"
c3 = "Subscribe this"
c4 = "Click this"
c = input("Enter Your Comment:\n")

if (c1 in c or c2 in c or c3 in c or c4 in c):
    print("It's a spam comment!")
else:
    print("Thanks for comment.")