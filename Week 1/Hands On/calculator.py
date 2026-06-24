def addition(a,b):
    return a+b
def substraction(a, b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if(a == 0):
        return "Error! Division by zero"
    return a/b

# Menu Display
print("Select Operation")
print("1. Add")
print("2. Substration")
print("3. Multiply")
print("4. Division")

# User Guide
choice = input("Enter choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values")
    exit()

# Operation execution
if choice == '1':
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {substraction(num1, num2)}")
elif choice == '3':
    print(f"{num1}* {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1}/{num2} = {division(num1, num2)}")
else:
    print("Invalid choice!")
