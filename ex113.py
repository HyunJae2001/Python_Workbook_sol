def inputData(lst):
    while True:
        string = input('Enter the string: ')

        if string == '':
            return lst
        else:
            lst.append(string)


def printData(lst):
    if len(lst) == 1:
        for i in lst:
            print(i)
    else:
        for i in range(len(lst)):
            if i == len(lst) - 1:
                print(lst[i])
            elif i == len(lst) - 2:
                print(lst[i], end=' and ')
            else:
                print(lst[i], end=', ')


def main():
    lst = []

    inputData(lst)
    printData(lst)


main()