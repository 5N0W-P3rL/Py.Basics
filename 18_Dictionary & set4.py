# Making a dictionary containing food list of 4 persons 

n1 = input("Enter name for person 1:")
n2 = input("Enter name for person 2:")
n3 = input("Enter name for person 3:")
n4 = input("Enter name for person 4:")
print("\n")

f1 = input("Enter Food name for person 1:")
f2 = input("Enter Food name for person 2:")
f3 = input("Enter Food name for person 3:")
f4 = input("Enter Food name for person 4:")
print("\n")

a  = {  "n1" : "f1",
        "n2" : "f2",
        "n3" : "f3",
        "n4" : "f4"
     }

print(a)                # --> Dictionary doesn't take input of person name [n1,n2,n3,n4] as key

# print("Order of person 1: ",a[n1])
# print("\n")
# print("Order of person 2: ",a[n2])
# print("\n")                          
# print("Order of person 3: ",a[n3])
# print("\n")
# print("Order of person 4: ",a[n4])
