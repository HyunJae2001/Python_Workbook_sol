string = input('Enter the string: ')

palindrome = True

for i in range(0, len(string)//2):
    if string[i] != string[-1-i]:
        palindrome = False
        break

print(palindrome)