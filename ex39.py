decibel = int(input('Enter a sound level in decibels: '))

if 40 <= decibel <= 130:
    if decibel >= 106:
        if decibel == 106:
            print('This is a gas lawnmower')
        elif decibel == 130:
            print('This is a jackhammer')
        else:
            print('This is between a gas lawnmower and a jackhammer')
    elif decibel >= 70:
        if decibel == 70:
            print('This is an alarm clock')
        else:
            print('This is between an alarm clock and a gas lawnmower')
    else:
        if decibel == 40:
            print('This is a Quiet room')
        else:
            print('This is between a quiet room and an alarm clock')
else:
    print('Out of range')