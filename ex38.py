month = input('Enter the name of a month: ')

month = month.title()

if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(f'{month} is the number of 30 days')
elif month == 'Febuary':
    print(f'{month} is the number of 28 or 29 days')
else:
    print(f'{month} is the number of 31 days')