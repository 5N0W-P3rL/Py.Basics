# Addition & Multiplication of Complex numbers:
# (a+bi)(c+di) = (ac−bd) + (ad+bc)i

r1 = int(input("Enter the real part of the complex number 1: "))
im1 = int(input("Enter the imaginary part of the complex number 1: "))
r2 = int(input("Enter the real part of the complex number 2: "))
im2 = int(input("Enter the imaginary part of the complex number 2: "))

c1 = [r1, im1]
c2 = [r2, im2]

class complex:
    def __init__(self, complx):
        self.real = complx[0]
        self.imaginary = complx[1]
    
    def __add__(self,c):
        complx = [self.real + c.real, self.imaginary + c.imaginary]
        return complex(complx)
    
    def __mul__(self,c):
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImaginary = self.real * c.imaginary + self.imaginary * c.real
        complx = [mulReal, mulImaginary]
        return complex(complx)
    
    def __str__(self):
        if self.imaginary < 0:
            return (f"{self.real} - {-self.imaginary}i")
        else:
            return (f"{self.real} + {self.imaginary}i")

cpx1 = complex(c1)
cpx2 = complex(c2)
print(f"1st Complex Number: {cpx1}")
print(f"2nd Complex Number: {cpx2}")
print(f"Sum of those Complex Numbers:")
print(f"{cpx1} + {cpx2} = {cpx1 + cpx2}")
print(f"Multiplication of those Complex Numbers:")
print(f"{cpx1} * {cpx2} = {cpx1 * cpx2}")