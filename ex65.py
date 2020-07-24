import math

distance = 0
x = int(input('Enter the x part of the coordinate: '))
y = int(input('Enter the y part of the coordinate: '))

x1 = x
y1 = y

while True:
    x2 = input('Enter the x part of the coordinate(blank to quit): ')

    if x2 == '':
        break

    y2 = input('Enter the y prat of the coordinate: ')
    x2 = int(x2)
    y2 = int(y2)

    distance += math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    x1 = x2
    y1 = y2

distance += math.sqrt(pow(x - x1, 2) + pow(y - y1, 2))

print(f'The perimeter of that polygon is {distance}')