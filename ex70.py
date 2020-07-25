message = input('Enter the message: ')
shift = int(input('Enter the shift amount: '))

for i in message:
    letter = chr(ord(i) - shift)
    if 'A' <= letter <= 'Z':
        print(letter, end='')
    elif 'a' <= letter <= 'z':
        print(letter, end='')
    else:
        print(i, end='')