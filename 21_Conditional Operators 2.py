# Pass - Fail Decision making calculator

sub1 = input("Enter Name of subject 1: ")
sub2 = input("Enter Name of subject 2: ")
sub3 = input("Enter Name of subject 3: ")
print("\n")
s1 = int(input("Enter Marks for subject 1: "))
s2 = int(input("Enter Marks for subject 2: "))
s3 = int(input("Enter Marks for subject 3: "))
h = int(input("Enter Highest Marks for each subject: "))

p_s1 = (s1/h)*100
p_s2 = (s2/h)*100
p_s3 = (s3/h)*100
percentage = (s1 + s2 + s3)/(h*3)*100
print ("Your Overall Percentage is:",percentage)

if (p_s1 >= 33 and p_s2 >= 33 and p_s3 >= 33 and percentage >= 40):
    print("You're successfully pass.")    

elif (p_s1 < 33 and p_s2 >= 33 and p_s3 >= 33):
    print("You're failed in",sub1)
    
elif (p_s1 >= 33 and p_s2 < 33 and p_s3 >= 33):
    print("You're failed in",sub2)

elif (p_s1 >= 33 and p_s2 >= 33 and p_s3 < 33):
    print("You're failed in",sub3)

else:
    print("You're failed in more than one subject.")
