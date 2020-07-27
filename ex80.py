import random

total = 0

for i in range(10):
    lst = [random.randrange(0, 2)]
    cnt = 0

    while cnt < 2:
        lst.append(random.randrange(0, 2))
        if lst[len(lst) - 1] == lst[len(lst) - 2]:
            cnt += 1
        else:
            cnt = 0

    for j in range(len(lst)):
        if lst[j] == 0:
            print('H', end=' ')
        else:
            print('T', end=' ')

    total += len(lst)
    print(f'({len(lst)} flips)')

print(f'On average, {total/10} flips were needed.')