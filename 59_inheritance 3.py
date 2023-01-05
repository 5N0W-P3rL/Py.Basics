# Example of property decorator & setter:

sl =  int(input("Enter the salary: "))
icr = float(input("Enter the increment: "))

class employee:
    def __init__(self, sl, icr):
        self.salary = sl
        self.increment = icr
        
    @property
    def salaryincrement(self):
        return (self.salary * self.increment)
    
    @salaryincrement.setter
    def salaryincrement(self, sai):
        increment = self.sai / self.salary
        
salary = employee(sl, icr)
print(f"Salary of the employee after increment: {salary.salaryincrement}")

sai = float(input("Enter the salary after increment: "))
salary.salaryincrement = sai
print(f"Your increment is {salary. increment}")

# Throws error for sai input