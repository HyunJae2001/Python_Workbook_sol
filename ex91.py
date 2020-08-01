def precedence(operator):
    operator = operator.strip()

    if operator[0] == '+' or operator[0] == '-':
        return 1
    elif operator[0] == '*' or operator[0] == '/':
        return 2
    elif operator[0] == '^':
        return 3
    else:
        return -1


operator = input('Enter the operator: ')
res = precedence(operator)

if res == -1:
    print('The input was not an operator')
else:
    print(res)