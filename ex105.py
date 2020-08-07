def main(lst):
    while True:
        n = int(input('Enter the integer number: '))

        if n == 0:
            break
        else:
            lst.append(n)

    return sorted(lst, reverse=True)


lst = []

print(main(lst))