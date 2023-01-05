# Find factorial of any number:

num = int(input("Enter the number: "))
fact = 1

for i in range(1,num+1):
    fact = i*fact

print(f"Factorial of {num}: {fact}")