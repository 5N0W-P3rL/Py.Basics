# Find Greatest number between four numbers:

n1 = int(input("Enter First number: ")) 
n2 = int(input("Enter next number: ")) 
n3 = int(input("Enter next number: ")) 
n4 = int(input("Enter next number: ")) 

if (n1 > n2 and n1 > n3 and n1 > n4) :
    print(str(n1) + " is greater. ")

elif (n2 > n1 and n2 > n3 and n2 > n4) :    
    print(str(n2) + " is greater. ")
    
elif (n3 > n2 and n3 > n1 and n3 > n4) :
    print(str(n3) + " is greater. ")
else :  
    print(str(n4) + " is greater. ")