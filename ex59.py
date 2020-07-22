string = input('Enter the string: ')

valid = True

if '0' <= string[0] <= '9':
    for i in range(1, 4):
        if '0' <= string[i] <= '9':
            continue
        else:
            valid = False
            break
    if valid == True:
        for i in range(4, 7):
            if 'A' <= string[i] <= 'Z':
                continue
            else:
                valid = False
                break
    if valid == True:
        print('New license plate')
    else:
        print('Cher your license plate')
else:
    for i in range(0, 3):
        if 'A' <= string[i] <= 'Z':
            continue
        else:
            valid = False
            break
    if valid == True:
        for i in range(3, 6):
            if '0' <= string[i] <= '9':
                continue
            else:
                print('Check your license plate')
                valid = False
                break
    if valid == True:
        print('Old license plate')
    else:
        print('Check your license plate')