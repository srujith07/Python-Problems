# Percentage Display
# Ask the user for a numerator and a denominator. Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        print("Error: Denominator cannot be zero.")
    else:
        percentage = (numerator / denominator) * 100
        print(f"The percentage is: {percentage:.2f}%")
except ValueError:
    print("Invalid input. Please enter numbers.")
