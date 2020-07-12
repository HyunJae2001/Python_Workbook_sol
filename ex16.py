import math

r = float(input('Enter a number of radius: '))

area = math.pi*pow(r, 2)
volume = (4/3)*math.pi*pow(r, 3)

print(f'The area of circle with a radius {r} is {area}')
print(f'The volume of circle with a radius {r} is {volume}')