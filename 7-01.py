# Dictionary of product prices
products = {"Laptop": 1200, "Phone": 800, "Tablet": 450}  # Dictionary with key-value pairs

# Using items to iterate through the dictionary
for product, price in products.items():  # Each tuple contains (key, value)
    print(f"The price of {product} is ${price}")  # Access key and value from the tuple
