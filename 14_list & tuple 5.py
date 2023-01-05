# Sum a list with 4 numbers

n1 = input("Enter first element:\n")
n2 = input("Enter next element:\n")
n3 = input("Enter next element:\n")
n4 = input("Enter next element:\n")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)

a = [n1,n2,n3,n4]
print("The list is:\n",a)
print(a[0] + a[1] +a[2] +a[3])
# print("Sum of elements of the list:",sum(a)) -->Alternate method using function.