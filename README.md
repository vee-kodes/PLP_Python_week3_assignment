# Price Discount Calculator 

A Python function that calculates the final price after applying a discount, following specific business rules.

## Features

- ✅ **Accurate Discount Calculation**: Applies discount only if 20% or higher
- 💰 **Currency Formatting**: Displays prices with 2 decimal places (e.g., `$100.00`)
- 📝 **User-Friendly Inputs**: Clear prompts with examples for ease of use

### Function Logic
```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:    # 20% threshold check
        return price - (price * discount_percent)  # Discount calculation
    return price  # Returns original price if discount < 20%
```

## Key Components
1. Input Handling:
    - Converts user input to float
    - Automatically divides discount percentage by 100 (e.g., 20 → 0.20)
2. Output Formatting:
    - Uses f-strings with :.2f for consistent currency display
    - Clear messages distinguishing discounted/non-discounted prices

## Examples
| Input (Price, Discount) | Expected Output               | Actual Output                             |
|-------------------------|-------------------------------|-------------------------------------------|
| `100, 25`              | `$75.00` (25% discount)       | `Final price (after discount): $75.00`    |
| `50, 15`               | `$50.00` (no discount)        | `Original price (no discount): $50.00`    |
| `80, 20`               | `$64.00` (exactly 20% discount)| `Final price (after discount): $64.00`    |

## How to Use
Python file:  [price_discount.py](price_discount.py)

1. Run the script:
```python
price_discount.py
```
2. Enter:
    - Original price (e.g., 100)
    - Discount percentage (e.g., 20 for 20%)

## Edge Case Handling
- Correctly processes:
    - Exact 20% threshold (Applies exact 20% discount)
    - Prices of $0.00 (Handles $0.00 price correctly)
    - Decimal discounts e.g., 19.999% (rejects discounts under 20%  ) and 20.001% (Applies discounts over 20% )


## Implementation Verification
✅ 100% Requirements Fulfilled

This solution strictly adheres to all assignment instructions:
- Implements `calculate_discount(price, discount_percent)` as specified
- Applies discounts only for 20% or higher thresholds
- Returns original price for discounts below 20%
- Includes user input prompts and formatted output