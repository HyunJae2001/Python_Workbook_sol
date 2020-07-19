magnitude = float(input('Enter a magnitude: '))

if magnitude <= 2:
    print(f'{magnitude} earthquake is considered to be a micro earthquake')
elif magnitude <= 3:
    print(f'{magnitude} earthquake is considered to be a very minor earthquake')
elif magnitude <= 4:
    print(f'{magnitude} earthquake is considered to be a minor earthquake')
elif magnitude <= 5:
    print(f'{magnitude} earthquake is considered to be a light earthquake')
elif magnitude <= 6:
    print(f'{magnitude} earthquake is considered to be a moderate earthquake')
elif magnitude <= 7:
    print(f'{magnitude} earthquake is considered to be a strong earthquake')
elif magnitude <= 8:
    print(f'{magnitude} earthquake is considered to be a major earthquake')
elif magnitude <= 10:
    print(f'{magnitude} earthquake is considered to be a great earthquake')
else:
    print(f'{magnitude} earthquake is considered to be a meteoric earthquake')