def tokenizing(string):
    lst = []
    index = -1

    for i in range(len(string)):
        if i == len(string) - 1:
            if index == -1:
                lst.append(string[i])
            else:
                lst.append(string[index:i+1])
        elif '0' <= string[i] <= '9' and i != len(string):
            if index == - 1:
                index = i
        else:
            lst.append(string[index:i])
            lst.append(string[i])
            index = -1

    lst = [i for i in lst if i != '' and i != ' ']

    return lst


def main():
    string = input('Enter the mathematical expression: ')

    print(tokenizing(string))


main()