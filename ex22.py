import math

s1 = float(input('Enter the length of the side: '))
s2 = float(input('Enter the length of the side: '))
s3 = float(input('Enter the length of the side: '))

s = (s1+s2+s3) / 2
area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print(f'The area of a triangle is {area}')