import random

A = []

for i in range(0, 101):
    A.append(random.randrange(1, 101))

cnt = 0
maximum = A[0]

for i in range(0, 101):
    if A[i] > maximum:
        print(f'{A[i]} <== Update')
        maximum = A[i]
        cnt += 1
    else:
        print(A[i])

print(f'The maximum value found was {maximum}')
print(f'The maximum value was updated {cnt} times')