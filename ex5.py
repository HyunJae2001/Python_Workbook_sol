UP_TO_ONE_LITER = 0.1
MORE_THAN_ONE_LITER = 0.25

up_to_one_liter = int(input('Enter the number of bottles that up to 1L: '))
more_than_one_liter = int(input('Enter the number of bottles that more than 1L: '))

total_deposit = up_to_one_liter*UP_TO_ONE_LITER + more_than_one_liter*MORE_THAN_ONE_LITER

print(f'total deposit is {total_deposit:.2f}')