letter = input('Enter a letter of the alphabet: ')

if letter in 'aeiou':
    print('Entered letter is a vowel')
elif letter in 'y':
    print('Sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('Entered letter is a consonant')