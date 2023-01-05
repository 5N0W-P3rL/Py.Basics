# Creating a class representing 3-D vector using a class of 2-D vector:
x = int(input("Enter the X-Cordinate:"))
y = int(input("Enter the y-Cordinate:"))
z = int(input("Enter the z-Cordinate:"))

class vector2d:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return f"{self.i}i + {self.j}j"

class vector3d(vector2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v2d = vector2d(x,y)
v3d = vector3d(x,y,z)

print(f"The 2D Vector: {v2d}")
print(f"The 3D Vector: {v3d}")