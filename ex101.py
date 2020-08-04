def engine(a, b):
    if a > b:
        for i in range(b, 0, -1):
            if a % i == 0 and b % i == 0:
                a //= i
                b //= i
    else:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                a //= i
                b //= i

    return a, b


numerator = int(input('Enter the numerator: '))
denominator = int(input('Enter the denominator: '))

numerator, denominator = engine(numerator, denominator)

print(f'{numerator}/{denominator}')