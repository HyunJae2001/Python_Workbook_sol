def convert(n):
    if n == 1:
        return 'first'
    elif n == 2:
        return 'second'
    elif n == 3:
        return 'third'
    elif n == 4:
        return 'fourth'
    elif n == 5:
        return 'fifth'
    elif n == 6:
        return 'sixth'
    elif n == 7:
        return 'seventh'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'ninth'
    elif n == 10:
        return 'tenth'
    elif n == 11:
        return 'eleventh'
    elif n == 12:
        return 'twelfth'
    else:
        return ''


num = int(input('Enter the integer number: '))

string = convert(num)

if string == '':
    print(f'{num} does not exist between 1 and 12')
else:
    print(f'{num} is {string} in ordinal number')