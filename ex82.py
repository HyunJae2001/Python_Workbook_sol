BASE = 4
PLUS = 0.25


def fare(distance):
    distance = (distance * 1000) / 140
    return BASE + PLUS * distance


distance = float(input('Enter the distance in kilometers: '))

charge = fare(distance)

print(f'Taxi fare is ${charge:.2f}')