import math

s = float(input('Enter the length of a side: '))
n = float(input('Enter the number of sides: '))

area = (n*pow(s, 2)) / (4*math.tan(math.pi/n))

print(f'The area of a regular polygon is {area}')