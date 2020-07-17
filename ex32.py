a, b, c = map(int, input('Enter a three numbers(a b c): ').split())

smallest = min(a, b, c)
largest = max(a, b, c)
middle = (a+b+c) - smallest - largest

print(f'The values ordered from smallest to largest are {smallest}, {middle}, {largest}')