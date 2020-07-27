string = list(input('Enter the binary: '))

cnt = 0
decimal = 0

if string.pop() == '1':
    decimal += 1

while string != []:
    binary = string.pop()
    cnt += 1
    if binary == '1':
        decimal += pow(2, cnt)

print(decimal)