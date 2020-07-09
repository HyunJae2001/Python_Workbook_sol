import math

a, b = map(int, input('Enter the two integers: ').split())

sum = a+b
dif = a-b
pro = a*b
quo = a//b
rem = a%b
log10 = math.log10(a)
pow = a**b

print(f'The sum of {a} and {b} is {sum}')
print(f'The difference when {b} is subtracted from {a} is {dif}')
print(f'The product of {a} and {b} is {pro}')
print(f'The quotient when {a} is divided by {b} is {quo}')
print(f'The remainder when {a} is divided by {b} is {rem}')
print(f'The result of log10({a}) is {log10}')
print(f'The result of {a}^{b} is %d{pow}')