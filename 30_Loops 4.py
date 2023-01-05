#  Find Whether a number is Prime or not:

num = int(input("Enter the number: "))
prime = True

for i in range(2,num):
    if (num % i == 0):
        prime = False
        break

if prime:
    print(str(num)+ " is Prime number.")
else:
    print(str(num)+ " is Non-Prime number.")