position = input('Enter a position: ')

column = position[0]
row = int(position[1])

if row%2 == 0:
    if column in 'aceg':
        print('White')
    else:
        print('Black')
else:
    if column in 'aceg':
        print('Black')
    else:
        print('White')