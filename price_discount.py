# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:    # 20% expressed as 0.20 (20/100)
        final_price = price - (price * discount_percent)
        return final_price
    else:
        return price   # returns the original price if discount < 20%


# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.

price = float(input('Enter the original price of the item (example 1000): '))
discount_percent = float(input('Enter discount (example 20 for 20%): ')) / 100 # divides discount by 100 


# Print the final price after applying the discount, or if no discount was applied, print the original price.

if discount_percent >= 0.20:
    #print(f'Discount applied: ${price * discount_percent:.2f}') # currency display in 2 decimal places
    print(f'Final price (after discount): ${calculate_discount(price, discount_percent):.2f}')
else:
    print(f'Original price (no discount): ${price:.2f}')
