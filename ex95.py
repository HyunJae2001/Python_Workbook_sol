import random


def generateLicense(n):
    license = ''

    if n == 0:
        for i in range(3):
            license += chr(random.randrange(ord('A'), ord('Z') + 1))
        for i in range(3):
            license += chr(random.randrange(ord('0'), ord('9') + 1))
    else:
        for i in range(4):
            license += chr(random.randrange(ord('0'), ord('9') + 1))
        for i in range(3):
            license += chr(random.randrange(ord('A'), ord('Z') + 1))

    return license


def main():
    print(generateLicense(random.randrange(0, 2)))


main()