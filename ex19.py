import math

gravity = 9.8

height = float(input('Enter the height of the object in meters: '))

vf = math.sqrt(2*gravity*height)

print(f'The final speed is {vf}m/s')