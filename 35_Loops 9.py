# print multiplication table of any number in reverse order:

n = int(input("Enter The number:"))

print("Multiplication table of " + str(n), ":")

for i in range (10,0,-1):
    print(f"{n} X {i} = {n*i}")