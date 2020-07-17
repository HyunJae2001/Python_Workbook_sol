LOWER = 10.5
LARGER = 4

n = float(input('Enter the human years: '))
dog_years = 0

if n<0:
    print('Wrong number')
else:
    if n > 2:
        n -= 2
        dog_years += (LOWER*2) + (LARGER*n)
    else:
        dog_years = LOWER * n
    print(f'The dog is {dog_years} years old')