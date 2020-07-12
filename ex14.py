FEET = 12
INCH = 2.54

feet = float(input('Enter a number of feet: '))
inches = float(input('Enter a number of inches: '))

centimeters = (feet*FEET + inches)*INCH

print(f'{feet}feet + {inches}inch = {centimeters:.2f}centimeter')