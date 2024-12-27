# Program to demonstrate division operation with error handling using if statement

# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the denominator is zero
if num2 == 0:
    # Provide an error message for division by zero
    print("Error: Division by zero is not allowed. Please provide a non-zero denominator.")
else:
    # Perform the division and print the result
    result = num1 / num2
    print(f"The result of division is: {result}")
1