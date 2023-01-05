# Cheek names in a list

p1 = input("Enter name of person 1:")
p2 = input("Enter name of person 2:")
p3 = input("Enter name of person 3:")
p4 = input("Enter name of person 4:")
p5 = input("Enter name of person 5:")
 
list = [p1, p2, p3, p4, p5]
print("Your list is:")
print(list)

cheek = input("Enter the name which will be searched: ")

if (cheek in list):
    print("The name is present in list.")
else:
    print("The name is not present in list.")