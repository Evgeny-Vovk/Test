try:
    # Try to open the file
    with open('non_existent_file.txt', 'r') as file:
        # Read the file's contents
        content = file.read()
        # Print the file's contents
        print(content)
except FileNotFoundError as e:
    # Print an error message if file is not found
    print(f"Error: The file could not be found.")