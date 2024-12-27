# Function to display catalog and calculate prices based on discount rules
def display_catalog():
    # Prices of individual items
    price_item1 = 200.0
    price_item2 = 400.0
    price_item3 = 600.0
    
    # Calculating combo prices
    combo1_price = (price_item1 + price_item2) * 0.90  # 10% discount
    combo2_price = (price_item2 + price_item3) * 0.90  # 10% discount
    combo3_price = (price_item1 + price_item3) * 0.90  # 10% discount
    gift_pack_price = (price_item1 + price_item2 + price_item3) * 0.75  # 25% discount
    
    # Displaying the catalog
    print("Online Store")
    print("-" * 45)
    print(f"Product(S)                               Price")
    print(f"Item 1                                   {price_item1:.2f}")
    print(f"Item 2                                   {price_item2:.2f}")
    print(f"Item 3                                   {price_item3:.2f}")
    print(f"Combo 1(Item 1 + 2)                      {combo1_price:.2f}")
    print(f"Combo 2(Item 2 + 3)                      {combo2_price:.2f}")
    print(f"Combo 3(Item 1 + 3)                      {combo3_price:.2f}")
    print(f"Combo 4(Item 1 + 2 + 3)                  {gift_pack_price:.2f}")
    print("-" * 45)
    print("For delivery contact: +(1)343-463-6040")

# Calling the function to display the catalog
display_catalog()