# Display marks of 6 students in sorted manner

n1 = input("Enter marks for student1 :\n")
n2 = input("Enter marks for student2 :\n")
n3 = input("Enter marks for student3 :\n")
n4 = input("Enter marks for student4 :\n")
n5 = input("Enter marks for student5 :\n")
n6 = input("Enter marks for student6 :\n")

marks_list = [n1,n2,n3,n4,n5,n6]

print("Marks of students:\n",marks_list)
marks_list.sort()
print("Sorted marks of students:\n",marks_list)