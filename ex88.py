def determine_triangle():
    a, b, c = map(int, input('Enter the three lengths: ').split())
    if a == max(a, b, c):
        if b + c > a:
            return True
        else:
            return False
    elif b == max(a, b, c):
        if a + c > b:
            return True
        else:
            return False
    else:
        if b + c > a:
            return True
        else:
            return False


print(determine_triangle())