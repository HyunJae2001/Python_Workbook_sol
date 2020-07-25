grade = input('Enter the letter grade: ')

total = 0
cnt = 0
avr = 0

while grade != '':
    if grade == 'A+':
        total += 4
    elif grade == 'A':
        total += 4
    elif grade == 'A-':
        total += 3.7
    elif grade == 'B+':
        total += 3.3
    elif grade == 'B':
        total += 3
    elif grade == 'B-':
        total += 2.7
    elif grade == 'C+':
        total += 2.3
    elif grade == 'C':
        total += 2
    elif grade == 'C-':
        total += 1.7
    elif grade == 'D+':
        total += 1.3
    elif grade == 'D':
        total += 1
    cnt += 1
    grade = input('Enter the letter grade(blank to quit): ')

avr = total / cnt

print(f'Average grade point is {avr}')