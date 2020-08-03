import random


def randomPassword():
    password = ''
    for i in range(random.randrange(7, 11)):
        password += chr(random.randrange(33, 127))
    return password


def checkPassword(string):
    if len(string) < 8:
        return False
    else:
        upper = False
        lower = False
        number = False

        for i in string:
            if upper == False and 'A' <= i <= 'Z':
                upper = True
            elif lower == False and 'a' <= i <= 'z':
                lower = True
            elif number == False and '0' <= i <= '9':
                number = True
            else:
                continue

        if upper == True and lower == True and number == True:
            return True
        else:
            return False


def main():
    cnt = 0
    while True:
        cnt += 1
        if checkPassword(randomPassword()) == True:
            return cnt


print(f'The number of attempts is {main()}')