# Function to calculate and print the circumference of a circle
def print_circum(radius):
    # Define π as a constant
    pi = 3.14159
    # Calculate the circumference
    circumference = 2 * pi * radius
    # Print the result
    print("The circumference of a circle with radius " + str(radius) + " is " + str(circumference))

# Calling the function with three different radiuses
print_circum(5)   # Radius = 5
print_circum(10)  # Radius = 10
print_circum(15)  # Radius = 15
