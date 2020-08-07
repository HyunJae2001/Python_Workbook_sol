def main():
    lst = list(map(int, input('Enter the integer numbers(a b c ...): ').split()))

    if len(lst) < 4:
        print('Please enters more than 3 values')
    else:
        lst.sort(reverse=True)
        return lst[2:-2]


print(main())