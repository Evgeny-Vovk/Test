def invert_dictionary(original_dict):  # Function to invert the given dictionary
    inverted_dict = {}  # Empty dictionary to store the result
    
    for student, courses in original_dict.items():  # Loop through each student and their courses
        for course in courses:  # Loop through each course for the current student
            if course not in inverted_dict:  # Check if the course is not yet a key in the inverted dictionary
                inverted_dict[course] = []  # Create a new key for the course with an empty list
            inverted_dict[course].append(student)  # Add the current student to the course's list
    
    return inverted_dict  # Return the inverted dictionary

# Original dictionary with students and their courses
original_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

print("Original Dictionary:")  # Label for the original dictionary
print(original_dict)  # Print the original dictionary

inverted_dict = invert_dictionary(original_dict)  # Call the function and store the result

print("\nInverted Dictionary:")  # Label for the inverted dictionary
print(inverted_dict)  # Print the inverted dictionary
