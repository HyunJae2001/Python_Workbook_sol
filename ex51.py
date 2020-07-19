grade = input('Enter a letter grade: ')

grade = grade.title()

if 'A' in grade:
    if '-' in grade:
        print('3.7')
    else:
        print('4.0')
elif 'B' in grade:
    if '+' in grade:
        print('3.3')
    elif '-' in grade:
        print('2.7')
    else:
        print('3.0')
elif 'C' in grade:
    if '+' in grade:
        print('2.3')
    elif '-' in grade:
        print('1.7')
    else:
        print('2.0')
elif 'D' in grade:
    if '+' in grade:
        print('1.3')
    else:
        print('1.0')
elif 'F' in grade:
    print('0')
else:
    print(f'{grade} does not exist in grade table')