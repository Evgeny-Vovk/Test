# Recursive countdown function
def countdown(n):
    # If the number reaches 0 or less, print 'Blastoff!'
    if n <= 0:
        print('Blastoff!')
    else:
        # Print the current number
        print(n)
        # Call countdown recursively with the number decreased by 1
        countdown(n - 1)

# Recursive countup function
def countup(n):
    # If the number reaches 0 or greater, print 'Blastoff!'
    if n >= 0:
        print('Blastoff!')
    else:
        # Print the current number
        print(n)
        # Call countup recursively with the number increased by 1
        countup(n + 1)

# Main program to get user input
# Prompt the user to enter a number
num = int(input("Enter a number (positive, negative, or zero): "))

# If the number is positive, call countdown
if num > 0:
    countdown(num)
# If the number is negative, call countup
elif num < 0:
    countup(num)
# If the number is zero, call countdown (choice explained below)
else:
    print("Zero detected, calling countdown:")
    countdown(num)
