# Find Multiplication table of any number:

def mult_table(n):
    for i in range (1,11):
        print(f"{n} X {i} = {n*i}")
    
n = int(input("Enter the number:"))
print(f"Multiplication table of {n}")
mult_table(n)