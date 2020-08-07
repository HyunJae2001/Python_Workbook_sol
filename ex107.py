def main():
    lst = []

    while True:
        word = input('Enter the word: ')

        if word == '':
            break
        else:
            if word in lst:
                continue
            else:
                lst.append(word)

    return lst


lst = main()

for i in lst:
    print(i)