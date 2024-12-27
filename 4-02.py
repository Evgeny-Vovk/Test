# Get user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

def rectangle_properties(length, width):
    if length <= 0 or width <= 0:
        print("Error: Both length and width must be positive numbers.")
    else:
        # Calculate area and perimeter
        area = length * width
        perimeter = 2 * (length + width)

        # Print out the results
        print(f"Calculated Area = {area:.2f}")
        print(f"Calculated Perimeter = {perimeter:.2f}")

# Call the function
rectangle_properties(length, width)
