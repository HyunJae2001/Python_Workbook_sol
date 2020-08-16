def Postfix(string):
    operators = []
    postfix = []

    for i in string:
        if i == '(':
            operators.append(i)
        elif i == ')':
            while True:
                operator = operators.pop()
                if operator == '(':
                    break
                postfix.append(operator)
        elif i == '+' or i == '-':
            if len(operators) > 0 and (operators[-1] == '*' or '-'):
                while True:
                    operator = operators.pop()

                    if operator == '(':
                        operators.append(operator)
                        break

                    postfix.append(operator)

                    if operators == []:
                        break
            operators.append(i)
        elif i == '*' or i == '/':
            operators.append(i)
        else:
            postfix.append(i)

    while operators != []:
        postfix.append(operators.pop())

    return postfix


def tokenizing(string):
    lst = []
    index = -1

    for i in range(len(string)):
        if i == len(string) - 1:
            if index == -1:
                lst.append(string[i])
            else:
                lst.append(string[index:i+1])
        elif '0' <= string[i] <= '9' and i != len(string):
            if index == - 1:
                index = i
        else:
            lst.append(string[index:i])
            lst.append(string[i])
            index = -1

    lst = [i for i in lst if i != '' and i != ' ']

    return lst


def main():
    string = input('Enter the mathematical expression: ')

    print(Postfix(tokenizing(string)))


main()