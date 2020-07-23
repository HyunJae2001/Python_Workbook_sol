n = int(input('Enter the integer number: '))

if n == 0:
    print('The first value is 0')
else:
    sum = 0
    cnt = 0

    while n != 0:
        sum += n
        cnt += 1
        n = int(input('Enter the integer number: '))

    avr = sum/cnt

    print(f'The average is {avr:.2f}')