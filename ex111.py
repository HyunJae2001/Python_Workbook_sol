def main():
    string = input('Enter the string: ')

    string = string.replace(',', '')
    string = string.replace('.', '')
    string = string.replace('?', '')
    string = string.replace('!', '')
    string = string.replace('-', '')
    string = string.replace(';', '')
    string = string.replace(':', '')

    words = string.split()

    return words


print(main())