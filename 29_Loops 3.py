#  Multiplication table of any number (using While Loop):

n = int(input("Enter The number:"))
i = 1

print("Multiplication table of " + str(n), ":")

while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i = i+1