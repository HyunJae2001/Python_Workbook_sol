def main():
    n = int(input('Enter the integer number: '))
    lst = []

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            lst.append(i)

    return lst


print(main())