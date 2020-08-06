def check_magicDate(year, month, date):
    if month * date == year % 100:
        display(year, month, date)


def find_lastDate(year, month):
    if month == 2:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

def display(year, month, date):
    if month == 1:
        month = 'January'
    elif month == 2:
        month = 'Febuary'
    elif month == 3:
        month = 'March'
    elif month == 4:
        month = 'April'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'June'
    elif month == 7:
        month = 'July'
    elif month == 8:
        month = 'August'
    elif month == 9:
        month = 'September'
    elif month == 10:
        month = 'October'
    elif month == 11:
        month = 'November'
    elif month == 12:
        month = 'December'

    print(f'{month} {date}, {year}')


def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            lastDate = find_lastDate(year, month)
            for date in range(1, lastDate + 1):
                check_magicDate(year, month, date)


main()