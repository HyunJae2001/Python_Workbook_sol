import random


def inputData(lst):
    while len(lst) < 6:
        n = random.randrange(1, 50)
        if n in lst:
            continue
        else:
            lst.append(n)

    lst.sort()

    return lst


def main():
    numbers = []

    print(inputData(numbers))


main()