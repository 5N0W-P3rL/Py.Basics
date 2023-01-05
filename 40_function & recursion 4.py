# Convert measurement from inches to centimeter:

def convert_in(n):
    return (2.54 * n)

n = int(input("Enter the measurement in Inches: "))
print(f"{n} in. = {convert_in(n)} cm.")