print('     ', end='')
for i in range(1, 11):
    print(f'{i:5d}', end='')
print()

for i in range(1, 11):
    print(f'{i:5d}', end='')
    for j in range(1, 11):
        print(f'{i*j:5d}', end='')
    print()