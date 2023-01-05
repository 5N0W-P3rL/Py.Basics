# Convert temperature from celsius to fahrenheit:

def convert_temp(temp):
    return ((temp*9/5)+32)
temp = int(input("Enter the temperature in Celsius:"))
print(f"{temp} Celsius = {convert_temp(temp)} Fahrenheit")