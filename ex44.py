month = input('Enter the month: ')
date = int(input('Enter the date: '))

month = month.title()

if month == 'January' and date == 1:
    print("New year's day")
elif month == 'July' and date == 1:
    print('Canada day')
elif month == 'December' and date == 25:
    print('Christmas day')
else:
    print('The entered month and day do not correspond to a fixed-date holiday')