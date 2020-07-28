FIRST = 10.95
SUB = 2.95


def cal_charge(n):
    return FIRST + (n - 1) * SUB


items = int(input('Enter the number of items: '))

charge = cal_charge(items)

print(f'The shipping charge is {charge}')