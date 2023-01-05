# Grade System:

# sub1 = input("Enter Name of the subject 1:") 
# sub2 = input("Enter Name of the subject 2:")
# sub3 = input("Enter Name of the subject 3:")
s1 = int(input("Enter Number in subject 1:" ))
s2 = int(input("Enter Number in subject 2:" ))
s3 = int(input("Enter Number in subject 3:" ))
h_marks = int(input("Enter hignest marks in each subject:" ))

percentage = (s1+s2+s3)/(h_marks*3)*100
print("Your Percentage is",percentage)

if (percentage >= 91 and percentage <= 100):
    print("Your Grade is 'Ex'")
elif (percentage >= 81 and percentage <= 90):
    print("Your Grade is 'A'")
elif (percentage >= 71 and percentage <= 80):
    print("Your Grade is 'B'")
elif (percentage >= 61 and percentage <= 70):
    print("Your Grade is 'C'")
elif (percentage >= 50 and percentage <= 60):
    print("Your Grade is 'D'")
elif (percentage < 50):
    print("Your Grade is 'F'")