month, date = map(str, input('Enter your birth day(month date): '))

month = month.title()
date = int(date)

"""MONTH = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in MONTH:
    for date in range(1, 32):
        print(f'{month} {date} ', end='')"""

if (month == 'December' and date >= 22) or (month == 'January' and date <= 19):
    print('Capricorn')
elif month == 'January' or (month == 'Febuary' and date <= 18):
    print('Aquarius')
elif month == 'Febuary' or (month == 'March' and date <= 20):
    print('Pisces')
elif month == 'March' or (month == 'April' and date <= 19):
    print('Aries')
elif month == 'April' or (month == 'May' and date <= 20):
    print('Taurus')
elif month == 'May' or (month == 'June' and date <= 20):
    print('Gemini')
elif month == 'June' or (month == 'July' and date <= 22):
    print('Cancer')
elif month == 'July' or (month == 'August' and date <= 22):
    print('Leo')
elif month == 'August' or (month == 'September' and date <= 22):
    print('Virgo')
elif month == 'September' or (month == 'October' and date <= 22):
    print('Libra')
elif month == 'October' or (month == 'November' and date <= 21):
    print('Scorpio')
else:
    print('Sagittarius')