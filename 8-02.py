# Function to read the dictionary from a file
def read_dict_from_file(file_path):
    """
    Reads a dictionary from a file.
    The file is expected to contain a valid Python dictionary.
    """
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            return eval(file.read())  # Read and evaluate the dictionary
    except Exception:
        return None  # Return None if there's an error

# Function to invert the dictionary
def invert_dictionary(original_dict):
    """
    Inverts a dictionary so that the keys become values and values become keys.
    If multiple keys share the same value, they are grouped into a list.
    """
    inverted = {}
    for key, value in original_dict.items():  # Iterate through key-value pairs
        if not isinstance(value, list):  # Ensure values are treated as lists
            value = [value]  # Convert single values to a list
        for item in value:
            inverted.setdefault(item, []).append(key)  # Group keys under each value
    return inverted

# Function to write a dictionary to a file
def write_dict_to_file(dictionary, file_path):
    """
    Writes a dictionary to a file in string format.
    """
    with open(file_path, 'w') as file:  # Open the file in write mode
        file.write(str(dictionary))  # Write the dictionary as a string

# Main function to execute the process
def main():
    input_file = 'input_dict.txt'  # Input file name
    output_file = 'output_dict.txt'  # Output file name

    original_dict = read_dict_from_file(input_file)  # Read the dictionary from the input file
    if original_dict is None:  # Check if reading failed
        return  # Exit if the dictionary couldn't be read

    inverted_dict = invert_dictionary(original_dict)  # Invert the dictionary
    write_dict_to_file(inverted_dict, output_file)  # Write the inverted dictionary to the output file

# Ensure the program runs only when executed directly
if __name__ == '__main__':
    main()
