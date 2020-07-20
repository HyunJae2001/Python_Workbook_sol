point = float(input('Enter a grade point: '))

if 4 <= point:
    print('A+')
elif 3.75 <= point:
    print('A')
elif 3.35 <= point:
    print('A-')
elif 3.05 <= point:
    print('B+')
elif 2.75 <= point:
    print('B')
elif 2.35 <= point:
    print('B-')
elif 2.05 <= point:
    print('C+')
elif 1.75 <= point:
    print('C')
elif 1.35 <= point:
    print('C-')
elif 1.05 <= point:
    print('D+')
elif 0.05 <= point:
    print('D')
else:
    print('F')