# Change Class Attribute

class verifier:
    a = 1

ob = verifier()
ob.a = 0

print(f"Object Attribute = {ob.a}")
print(f"Class Attribute = {verifier.a}")

if (ob.a == verifier.a):
    print("Class Attribute is changed.")
else:
    print("Class Attribute is not changed.")