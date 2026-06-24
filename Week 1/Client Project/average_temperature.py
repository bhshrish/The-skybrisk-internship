def calculate_average_temperature():
    n = int(input("How many temperature readings do you want to enter? "))

    temperatures = []

    for i in range(n):
        temp = float(input(f"Enter temperature {i + 1}: "))
        temperatures.append(temp)

    average = sum(temperatures) / len(temperatures)

    print(f"\nAverage Temperature: {average:.2f}°C")


if __name__ == "__main__":
    calculate_average_temperature()
