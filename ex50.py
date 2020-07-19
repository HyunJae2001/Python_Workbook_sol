import math

a, b, c = map(int, input('Enter the values of a, b, and c (a b c): ').split())

distinction = pow(b, 2) - (4*a*c)

if distinction < 0:
    print('Does not have any real roots')
elif distinction == 0:
    root = (-b) / (2*a)
    print('Has one real root')
    print(f'It is {root}')
else:
    root1 = (-b-math.sqrt(distinction)) / (2*a)
    root2 = (-b+math.sqrt(distinction)) / (2*a)
    print('Hs two real roots')
    print(f'It is {root1} and {root2}')