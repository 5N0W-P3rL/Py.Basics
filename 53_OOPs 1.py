# information storing of a programmer: 

company = input("Enter the name of the company:")

class programmer:
    def __init__(self, name, product, salary):
        self.name = name 
        self.product = product
        self.salary = salary
    
    def info(self):
       print(f"{self.name} is working on {self.product} at {company} & his salary is {self.salary}k.")

nm1 = input("Enter the name of the programmer:")
sl = input("Enter the salary of the programmer:")
pd = input("Enter the working product of the programmer:")

pro = programmer(nm1, pd, sl)
pro.info()