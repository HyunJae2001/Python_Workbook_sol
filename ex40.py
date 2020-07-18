side1 = int(input('Enter the length of side1: '))
side2 = int(input('Enter the length of side2: '))
side3 = int(input('Enter the length of side3: '))

if side1 == side2 and side2== side3:
    print('Equilateral triangle')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('Isosceles triangle')
else:
    print('Scalene triangle')