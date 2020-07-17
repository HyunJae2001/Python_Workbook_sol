PRICE = 3.49
DISCOUNT = 0.6

n = int(input('Enter the number of loaves of day old bread: '))

regular = n * PRICE
discount = regular * DISCOUNT
total = regular - discount

print(f'The regular price is {regular:.2f}')
print(f'The discount prise is {discount:.2f}')
print(f'The total price is {total:.2f}')