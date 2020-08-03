import random


def randomPassword():
    password = ''
    for i in range(random.randrange(7, 11)):
        password += chr(random.randrange(33, 127))
    return password


print(randomPassword())