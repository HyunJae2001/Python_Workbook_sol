while True:
    bits = input('Enter the 8 bits: ')
    if bits == '':
        break
    else:
        if (bits.count('1') + bits.count('0') != 8) or len(bits) != 8:
            print('Check your input')
        else:
            if bits.count('1') % 2 == 1:
                print('Selected the odd parity')
            else:
                print('Selected the even parity')