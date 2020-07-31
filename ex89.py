def capitalize(string):
    string = list(string)
    first = True

    for i in range(len(string)):
        if first == True and 'a' <= string[i] <= 'z':
            string[i] = string[i].upper()
            first = False
        else:
            if string[i] == 'i':
                if string[i-1] == ' ' and string[i+1] == ' ':
                    string[i] = string[i].upper()
            elif string[i] == '.' or string[i] == '?' or string[i] == '!':
                first = True

    return string


string = input('Enter the string: ')
string = capitalize(string)

for i in range(len(string)):
    print(string[i], end='')