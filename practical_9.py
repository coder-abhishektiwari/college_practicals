#Practical 9: Write a Python program to convert temperatures to and from Celsius, Fahrenheit. 
#[ Formula: c/5 = f-32/9] 
print()
print("Program of conversion between Celsius and Fahrenheit\n")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example Conversion
celsius = 25  # Celsius temperature
fahrenheit = 77  # Fahrenheit temperature

# Directly print both conversions
print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
print()