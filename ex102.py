TEA = 1
TABLE = TEA * 3
CUP = TABLE * 16


def cal(tea):
    cup = 0
    table = 0

    while tea >= CUP:
        cup += 1
        tea -= CUP

    while tea >= TABLE:
        table += 1
        tea -= TABLE

    return cup, table, tea


tea = int(input('Enter the number of teaspoons: '))

print('%d cup, %d tablespoons, %d teaspoons' %cal(tea))