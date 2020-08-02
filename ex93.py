import math


def checkPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def nextPrime(n):
    while True:
        n += 1
        if checkPrime(n):
            return n


def main():
    n = int(input('Enter the number: '))

    print(nextPrime(n))


main()