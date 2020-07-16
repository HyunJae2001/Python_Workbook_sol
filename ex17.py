C = 4.186
JtokWh = 2.7777777778e-7
KWH = 8.9

mass = float(input('Enter the mass of the water: '))
delT = float(input('Enter the amount of temperature change: '))

j = mass*C*delT
kWh = j*JtokWh
cost = kWh*KWH

print(f'The cost of boiling water is {cost}cent')