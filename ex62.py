DISCOUNT = 0.6
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for i in original_prices:
    discount_amount = i * DISCOUNT
    discount_price = i - discount_amount
    print(f'Original price is ${i}')
    print(f'Discount amount is ${discount_amount:.2f}')
    print(f'Discount price is ${discount_price:.2f}\n')