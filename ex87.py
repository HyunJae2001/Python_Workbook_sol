WIDTH = 100


def return_new_string(string):
    new = ' ' * ((WIDTH - len(string)) // 2) + string

    return new


def input_string():
    string = input('Enter the string: ')
    print(return_new_string(string))


input_string()