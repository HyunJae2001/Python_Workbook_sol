import math


def check_prime():
    n = int(input('Enter the number: '))

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


print(check_prime())