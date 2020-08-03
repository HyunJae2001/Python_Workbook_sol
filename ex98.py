def hex2int(n):
    return int(n, 16)


def int2hex(n):
    return hex(n)


def main():
    n = input('Enter the hex number: ')
    print(hex2int(n))

    n = int(input('Enter the int number: '))
    print(int2hex(n))


main()