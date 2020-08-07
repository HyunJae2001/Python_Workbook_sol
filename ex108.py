def main():
    lst = list(map(int, input('Enter the integer numbers: ').split()))

    for i in range(len(lst)):
        lst[i] = lst[i] * -1

    return sorted(lst)


print(main())