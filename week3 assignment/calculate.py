def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage to be applied
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Get user input and handle potential errors
try:
    original_price = float(input("Enter the original price: $"))
    discount = float(input("Enter the discount percentage: "))
    
    if original_price < 0 or discount < 0:
        print("Price and discount must be positive numbers.")
    else:
        final_price = calculate_discount(original_price, discount)
        
        if final_price == original_price:
            print(f"\nNo discount applied. Original price: ${original_price:.2f}")
        else:
            savings = original_price - final_price
            print(f"\nOriginal price: ${original_price:.2f}")
            print(f"Discount applied: {discount}%")
            print(f"Final price: ${final_price:.2f}")
            print(f"You save: ${savings:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")