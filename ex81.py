import math

def Pythagorean(l1, l2):
    return math.sqrt(pow(l1, 2) + pow(l2, 2))


l1, l2 = map(int, input('Enter the lengths of the two shorter side: ').split())

hypotenuse = Pythagorean(l1, l2)

print(f'The hypotenuse of a right triangle is {hypotenuse}')