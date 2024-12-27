def get_number():
    # Returns a number or None
    return None

# Misusing the return value
result = get_number()
print(result + 5)  # Attempting to add None to a number causes a crash
