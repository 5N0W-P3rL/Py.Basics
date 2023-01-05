# Greeting for the persons whose names startswith 's':

nm1 = input("Enter name of the person 1: ")
nm2 = input("Enter name of the person 2: ")
nm3 = input("Enter name of the person 3: ")
nm4 = input("Enter name of the person 4: ")
nm5 = input("Enter name of the person 5: ")

l1 = [nm1, nm2, nm3, nm4, nm5]

for name in l1:
    if name.startswith("S"):
        print("Hello " +name)