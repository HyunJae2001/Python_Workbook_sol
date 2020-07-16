R = 8.314

P = float(input('Enter the pressure in pascal: '))
V = float(input('Enter the volume in liter: '))
T = float(input('Enter the temperature in C: '))

mole = (P*V) / (R*T)

print(f'The amount of gas is {mole} mole')