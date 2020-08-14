def check(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


def main():
    lst = list(map(int, input('Enter the numbers(a b c ...): ').split()))

    print(check(lst))


main()