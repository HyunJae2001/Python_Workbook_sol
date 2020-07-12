CENTS = int(input('Enter a number of cents: '))
cents = CENTS

toonies = cents // 200
cents -= toonies * 200

loonies = cents // 100
cents -= loonies * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

print(f'{CENTS} cents is {toonies} toonies {loonies} loonies {quarters} quarters {dimes} dimes {nickels} nickels {pennies} pennies')