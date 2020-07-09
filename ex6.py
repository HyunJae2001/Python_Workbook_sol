TAX = 0.1
TIP = 0.18

cost = float(input('Enter the cost of a meal ordered: '))

tax = cost*TAX
tip = cost*TIP
total = cost + tax + tip

print('The amount of a tax is %.2f and the amount of a tip is %.2f and the total amount of a meal is %.2f' %(tax, tip, total))