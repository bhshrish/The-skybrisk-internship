# Taking input safely with validation
def read_int(prompt):
    while True:
        try:
            value = int(input(prompt)) # convert input to integer
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer")

# Read values
name = input("Enter your name: ") #Simple string input
age = read_int("Enter you age: ") #Validated integer input

print("Hello,", name)
print("You are", age, "years old")

# string input
name = input("Enter your name: ")
print("Hello", name)

# Integer input
age = int(input("Enter your age:"))
print("You are", age,"years old.")

# Mulitple inputs in one line
x,y = input("Enter two values: ").split()
print("First:",x, "Second:", y)