# Multiplication table of any number:

n = int(input("Enter The number:"))

print("Multiplication table of " + str(n), ":")
for i in range (1,11):
    print(f"{n} X {i} = {n*i}")