def search_median(a, b, c):
    if a == b == c:
        return a
    elif a != b != c:
        if a < b < c or c < b < a:
            return b
        elif b < a < c or c < a < b:
            return a
        else:
            return c
    else:
        if a == b:
            return a
        elif b == c:
            return b
        else:
            return a


a, b, c = map(int, input('Enter the three numbers: ').split())

middle = search_median(a, b, c)

print(f'The median number is {middle}')