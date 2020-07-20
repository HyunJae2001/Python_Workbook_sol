frequency = float(input('Enter the frequency: '))

if frequency < 3*pow(10, 9):
    print('Radio waves')
elif frequency < 3*pow(10, 12):
    print('Microwaves')
elif frequency < 4.3*pow(10, 14):
    print('Infrared light')
elif frequency < 7.5*pow(10, 14):
    print('Visible light')
elif frequency < 3*pow(10, 17):
    print('Ultraviolet light')
elif frequency < 3*pow(3, 19):
    print('X-rays')
else:
    print('Gamma rays')