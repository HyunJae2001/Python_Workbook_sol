def binary(n, lst):
    if n > 1:
        binary(n // 2, lst)

    lst.append(n % 2)

    return lst


n = int(input('Enter the decimal: '))

res = binary(n, list())

for i in range(0, len(res)):
    print(res[i], end='')