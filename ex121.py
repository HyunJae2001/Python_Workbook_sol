def countRange(lst, minimum, maximum):
    cnt = 0

    for i in lst:
        if minimum <= i <= maximum:
            cnt += 1

    return cnt


def main():
    lst = list(map(int, input('Enter the numbers(a b c...): ').split()))
    minimum = int(input('Enter the minimum value: '))
    maximum = int(input('Enter the maximum value: '))

    print(f'The number between {minimum} and {maximum} is {countRange(lst, minimum, maximum)}')


main()