# Making calculator for finding square, cube & Square-root:

num = int(input("Enter the number:"))

class calculator:
    def __init__(self,num):
        self.num = num
        
    def square(self):
        print(f"Square of {self.num} = {self.num **2}")
    
    def cube(self):
        print(f"Cubee of {self.num} = {self.num **3}")
    
    def squareroot(self):
        print(f"Square-root of {self.num} = {self.num **0.5}")
    
    @staticmethod
    def greet():
        print("##### Hello! Results are shown below. #####")

calc = calculator(num)

calc.greet()
calc.square()
calc.cube()
calc.squareroot()