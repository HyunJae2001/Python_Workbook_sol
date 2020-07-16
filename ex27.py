height = float(input('Enter the height in meters: '))
weight = float(input('Enter the weight in kilograms: '))

BMI = weight / pow(height, 2)

print(f'Your BMI is {BMI}')