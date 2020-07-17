n = int(input('Enter a number of sides: '))

if 3 <= n <= 10:
    if n == 3:
        print('Triangle')
    elif n == 4:
        print('Quadrilateral')
    elif n == 5:
        print('Pentagon')
    elif n == 6:
        print('hexagon')
    elif n == 7:
        print('Heptagon')
    elif n == 8:
        print('Octagon')
    elif n == 9:
        print('Nonagon')
    else:
        print('Decagon')
else:
    print('Out of range')