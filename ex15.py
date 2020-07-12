INCH = 12
YARD = 0.333333
MILE = 0.000189394

feet = float(input('Enter a number of feet: '))

inch = feet*INCH
yard = feet*YARD
mile = feet*MILE

print(f'{feet}feet is {inch}inch, {yard}yard, {mile}mile')