#Basic if statement example
x = 10
if x > 5:
    print("x is greater than 5")
#if-else statement
x = 3
if x >=5:
    print("x is 5 or more")
else:
    print("x is less than 5")

num = 0

if num > 0:
    print("Postive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Nested if example
age = 20

if age > 0:
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
else:
    print("Invalid age")

#Inline conditional expression
a = 5
b = 10

result = "a is smaller" if a < b else "a is not smaller"
print(result)

# Program demonstrating conditional statements with input validations
def safe_int_input(prompt):
    """Reads an integer safely from the user."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please return an integer.")
        return None
num = safe_int_input("Enter a number")

if num is not None:
    if num > 0:
        print("The number is postive.")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero.")