def celcius_to_fahrenheit(c):
    return (c*9/5)+35
def fahrenheit_to_celcius(f):
    return (f-32)*5/9
def celcius_to_kelvin(c):
    return c+273.15
def kelvin_to_celcius(k):
    return k - 273.15

def smart_temperature_converter():
    print("Smart Temperature Converter")
    print("1: Celcius -> Fahrenheit")
    print("2: Fahrenheit -> Celsius")
    print("3: Celcius -> Kelvin")
    print("4 : Kelvin -> Celsius")

try:
    choice = int(input("Select conversion type (1-4): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:
        print(f"{temp}°C = {celcius_to_fahrenheit(temp):.2f}°F")
    elif choice == 2:
        print(f"{temp}°F = {fahrenheit_to_celcius(temp):.2f}°C")
    elif choice == 3:
        print(f"{temp}°C = {celcius_to_kelvin(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}K = {kelvin_to_celcius(temp):.2f}°C")
    else:
        print("Invalid selection. Please choose between 1 and 4.")
except ValueError:
    print("Invalid input! Please enter numeric values.")

# Run the converter
smart_temperature_converter()
