# cheeking for tuple immutablity


n1  = input("Enter first element:")
n2  = input("Enter next element:")
n3  = input("Enter next element:")
n4  = input("Enter next element:")

tup1 = (n1,n2,n3,n4)
print("Tuple before implementation:",tup1)

tup1[1] = 32
print("Tuple after implementation:",tup1)
