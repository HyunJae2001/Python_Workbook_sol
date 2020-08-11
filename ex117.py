def cal_b(X, Y, m):
    x = sum(X) / len(X)
    y = sum(Y) / len(Y)

    return y - m * x


def cal_m(X, Y):
    n = len(X)
    x_square_total = 0
    x_total_square = sum(X) ** 2
    xy_total = 0
    x_total = sum(X)
    y_total = sum(Y)

    for i in range(n):
        x_square_total += X[i] ** 2
        xy_total += X[i] * Y[i]

    return (xy_total - (x_total * y_total) / n) / (x_square_total - (x_total_square) / n)



def inputData(X, Y):
    while True:
        x = input('Enter the x value: ')

        if x == '':
            break

        y = input('Enter the y value:' )

        X.append(float(x))
        Y.append(float(y))


def main():
    X = []
    Y = []

    inputData(X, Y)
    m = cal_m(X, Y)
    b = cal_b(X, Y, m)

    print(f'y = {m:.2f}x + {b:.1f}')


main()