# Simple program to display name and perform operations
def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

# Input: Accepting the user's name and an integer n
name = input("Enter your name: ")
n = int(input("Enter the number of characters to display from the left: "))

# Operation 1: Display n characters from the left
if n > 0:
    print("First", n, "characters:", name[:n])
else:
    print("Invalid input for n. It must be greater than 0.")

# Operation 2: Count the number of vowels in the name
vowel_count = count_vowels(name)
print("Number of vowels in the name:", vowel_count)

# Operation 3: Reverse the name
reversed_name = ""
for char in name:
    reversed_name = char + reversed_name
print("Reversed name:", reversed_name)
