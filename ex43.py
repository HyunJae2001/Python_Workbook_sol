banknote = int(input('Enter the denomination of a banknote in dollar: '))

if banknote == 1:
    print('George Washington')
elif banknote == 2:
    print('Thomas Jefferson')
elif banknote == 5:
    print('Abraham Lincoln')
elif banknote == 10:
    print('Alexander Hamilton')
elif banknote == 20:
    print('Andrew Jackson')
elif banknote == 50:
    print('Ulysses S.Grant')
elif banknote == 100:
    print('Benjamin Franklin')
else:
    print('This banknote does not exist')