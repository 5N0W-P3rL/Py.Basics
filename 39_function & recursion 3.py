# Find sum of natural numbers upto 'n' using recursion:

def n_Sum(num):
    if (num == 0):
        return 0
    return num + n_Sum(num - 1)
    #return (sum)

n = int(input("Enter the last number: "))
print(f"Sum of natural numbers from 1 to {n}: {n_Sum(n)}")
