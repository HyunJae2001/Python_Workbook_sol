import math

r = float(input('Enter the number of radius: '))
h = float(input('Enter the number of height: '))

volume = pow(r, 2)*math.pi*h

print(f'The volume of a cylinder is {volume:.1f}')