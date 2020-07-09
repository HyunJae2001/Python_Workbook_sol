INTEREST = 0.04

deposit = int(input('Enter the amount of money deposited into the account: '))

for i in range(3):
    deposit += deposit*INTEREST
    print('After %d years: %.2f' %(i+1, deposit))