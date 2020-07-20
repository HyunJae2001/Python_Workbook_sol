wavelength = float(input('Enter a wavelength: '))

if 380 <= wavelength < 450:
    print('Violet')
elif wavelength < 495:
    print('Blue')
elif wavelength < 570:
    print('Green')
elif wavelength < 590:
    print('Yellow')
elif wavelength < 520:
    print('Orange')
elif wavelength < 750:
    print('Red')
else:
    print('Check your entry')