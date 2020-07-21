year, month, date = map(int, input('Enter the date: ').split('-'))

if month == 2:
    if date == 28:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            date += 1
    else:
        date = 1
        month += 1
else:
    if month == 12:
        if date == 31:
            date = 1
            month = 1
            year += 1
        else:
            date += 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date == 30:
            date = 1
            month += 1
        else:
            date += 1
    else:
        if date == 31:
            date = 1
            month += 1
        else:
            date += 1

print(f'{year}-{month:02d}-{date:02d}')