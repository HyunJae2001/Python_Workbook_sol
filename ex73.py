string = input('Enter the string: ')

palindrome = True
start = 0
end = len(string) - 1

while start < end:
    if string[start] == ' ':
        start += 1
    elif string[end] == ' ':
        end -= 1
    elif string[start] != string[end]:
        palindrome = False
    else:
        start += 1
        end -= 1

print(palindrome)