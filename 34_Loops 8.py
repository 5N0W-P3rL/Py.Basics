# Print this Pattern:
#     *
#    ***
#   *****

n = int(input("Enter The number of rows: "))

for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
    