import math

t1 = float(input('Enter the x value of a point on Earth in degrees: '))
g1 = float(input('Enter the y value of a point on Earth in degrees: '))
t2 = float(input('Enter the x value of a second point on Earth in degrees: '))
g2 = float(input('Enter the y value of a second point on Earth in degrees: '))

distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print(f'Distance between two points on Earth is {distance}km')