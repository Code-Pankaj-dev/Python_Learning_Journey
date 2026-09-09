# Task: Smart Temperature Converter
# Question: Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.
# (Use explicite type conversion and arithmetic operations.)

# Formula = (C * 9/5) + 32 for Fahrenheit, 
# C + 273.15 for Kelvin....
Celsius = float(input("Enter Temprature in Celsius:"))

Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

print("Celsius to Fahrenheit Value: ", Fahrenheit)
print("Celsius to Kelvin Value: ", Kelvin)