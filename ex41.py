name_of_note = input('Enter the name of note: ')

name_of_note = name_of_note.title()
note = name_of_note[0]
x = int(name_of_note[1])

if note == 'C':
    frequency = 261.63
elif note == 'D':
    frequency = 293.66
elif note == 'E':
    frequency = 329.63
elif note == 'F':
    frequency = 349.23
elif note == 'G':
    frequency = 392.00
elif note == 'A':
    frequency = 440.00
elif note == 'B':
    frequency = 493.88

frequency /= 2**(4-x)

print(f'{name_of_note} is {frequency} Hz')