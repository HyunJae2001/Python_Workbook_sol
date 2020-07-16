days = int(input('Enter a number of days: '))
hours = int(input('Enter a number of hours: '))
minutes = int(input('Enter a number of minutes: '))
seconds = int(input('Enter a number of seconds: '))

total = seconds + (minutes*60) + (hours*60*60) + (days*60*60*24)

print(f'{days} days {hours} hours {minutes} minutes {seconds} seconds is {total}seconds')