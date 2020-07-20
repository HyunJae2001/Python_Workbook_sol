RAISE = 2400
UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

rating = float(input('Enter a rating: '))

if rating == UNACCEPTABLE:
    print('Unacceptable performance')
    print('Raise of $%.2f' %(RAISE*rating))
elif rating == ACCEPTABLE:
    print('Acceptable performance')
    print('Raise of $%.2f' %(RAISE*rating))
elif rating >= MERITORIOUS:
    print('Meritorious performance')
    print('Raise of $%.2f' %(RAISE*rating))
else:
    print('Check your rating')