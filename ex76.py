n = int(input('Enter an integer(2 or greater): '))

factor = 2

print(f'The prime factors of {n} are:')

while n > 1:
    if n % factor == 0:
        print(f'{factor}')
        n //= factor
    else:
        factor += 1