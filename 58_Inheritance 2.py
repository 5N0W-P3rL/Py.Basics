# Example of a multilevel inheritance:

class Animals:
    type = "Mamals"

class Pets(Animals):
    colour = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
print(f"Colour of the dog: {d.colour}")
d.bark()
