CHILD = 14
SENIOR = 18
OTHER = 23

total = 0

while True:
    age = input('Enter the age: ')
    if age == '':
        break
    else:
        age = int(age)
        if age <= 2:
            continue
        elif 3 <= age <= 12:
            total += CHILD
        elif age >= 65:
            total += SENIOR
        else:
            total += OTHER

print(f'The admission cost for the group is ${total:.2f}')