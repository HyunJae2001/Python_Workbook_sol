def checker(month, year):
    if 1 <= month <= 12:
        if month == 2 and (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
            return 29
        elif month == 2:
            return 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        else:
            return 31
    else:
        return -1


def main():
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))

    date = checker(month, year)

    if date == -1:
        print('Check your input')
    else:
        print(date)


main()