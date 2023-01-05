# Cheeking length of an username:

username = input("Enter your username:")
len_Uname = len(username)
print("Length of your username:",len_Uname)

if (len_Uname < 10):
    print("Your username is containing less than 10 charecter!")
else :
    print("Your username is good.") 