# Print this pattern using function:
#     ****
#     ***
#     **
#     *

def prt_pattern(n):
    for i in range(n):
        print("*" * (n-i))
    
n = int(input("Enter the number of rows: "))
prt_pattern(n)