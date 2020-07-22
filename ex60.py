import random

n = random.randrange(0, 38)

if n == 0:
    print('Pay 0')
elif n == 37:
    print('Pay 00')
else:
    print(f'Pay {n}')

if n != 0 and n != 37:
    if (n%2 == 1 and (n < 10 or 18 < n <28)) or (n%2 == 0 and (10 < n < 19 or 29 < n < 37)):
        print('Red')
    else:
        print('Black')

    if n%2 == 0:
        print('Even')
    else:
        print('Odd')

    if n <= 18:
        print('1 to 18')
    else:
        print('19 to 36')