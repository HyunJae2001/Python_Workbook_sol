C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

frequency = float(input('Enter a frequency: '))

if C4-1 <= frequency <= C4+1:
    print('This frequency is C note')
elif D4-1 <= frequency <= D4+1:
    print('This frequency is D note')
elif E4-1 <= frequency <= E4+1:
    print('This frequency is E note')
elif F4-1 <= frequency <= F4+1:
    print('This frequency is F note')
elif G4-1 <= frequency <= G4+1:
    print('This frequency is G note')
elif A4-1 <= frequency <= A4+1:
    print('This frequency is A note')
elif B4-1 <= frequency <= B4+1:
    print('This frequency is B note')
else:
    print('This frequency does not correspond to a known note')