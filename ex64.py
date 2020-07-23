total_price = 0

while True:
    price = input('Enter the price: ')

    if price == '':
        break
    else:
        total_price += float(price)

print(f'The total price is {total_price}')

pennies = total_price * 100

if pennies % 5 < 2.5:
    pennies -= pennies % 10
else:
    pennies += 10 - pennies % 10

print(f'The total number of pennie is {pennies}')
print(f'The total number of nickel is {pennies/5}')