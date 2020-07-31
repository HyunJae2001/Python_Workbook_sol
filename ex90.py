def isInteger(string):
    string = string.strip()

    if string[0] == '-' or string[0] == '+':
        return string[1:].isdigit()
    else:
        return string.isdigit()


string = input('Enter the string: ')
print(isInteger(string))