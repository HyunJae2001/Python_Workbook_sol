month = input('Enter the name of the month: ')
date = int(input('Enter the date: '))

month = month.title()

"""MONTH = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in MONTH:
    for date in range(1, 32):
        print(f'{month} {date} ', end='')"""

if (month == 'March' and date >= 20) or month == 'April' or month == 'May' or (month == 'June' and date < 21):
    print('Spring')
elif month == 'June' or month == 'July' or month == 'August' or (month == 'September' and date < 22):
    print('Summer')
elif month == 'September' or month == 'November' or month == 'October' or (month == 'December' and date < 21):
    print('Fall')
else:
    print('Winter')