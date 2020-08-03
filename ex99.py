def converter(n):
    return chr(63 + n)


def main():
    base = int(input('Enter the cumber: '))

    if 2 <= base <= 16:
        convert = converter(base)
        print(f'Base number is {base}')
        print(f'Convert number is {convert}')
    else:
        print('Out of range')


main()