temp = float(input('Enter the air temperature: '))
wind = float(input('Enter the wind speed: '))

wci = 13.12 + (0.6215*temp) - (11.37*pow(wind, 0.16)) + (0.3965*temp*pow(wind, 0.16))
wci = round(wci)

print(f'The WCI is {wci}')