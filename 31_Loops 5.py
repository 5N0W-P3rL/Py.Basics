# Find Sum of natural numbers in a given range:

num = int(input("Enter the range value: "))
sum = 0
i = 1
while i <= num:
    sum = sum+i
    i = i+1
    
print(f"Sum of all natural numbers between 1 to {num} = {sum}.")