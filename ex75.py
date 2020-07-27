n, m = map(int, input('Enter the two positive integers: ').split())

d = min(n, m)

while n%d != 0 or m%d != 0:
    d -= 1

print(f'The greatest common divisor is {d}')