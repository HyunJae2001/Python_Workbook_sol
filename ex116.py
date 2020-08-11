def consonant(word):
    if not 'a' <= word[-1] <= 'z':
        last = word[-1]
        word = word.rstrip(word[-1])
    for i in range(len(word)):
        if word[i] in 'aeiou':
            word += word[0:i]
            word = word.lstrip(word[0:i])
            break

    return word.title() + 'ay' + last


def vowel(word):
    if not 'a' <= word[-1] <= 'z':
        last = word[-1]
        word = word.rstrip(word[-1])

    return word.title() + 'way' + last


def check(word):
    if word[0] in 'aeiou':
        return True

    return False


def main():
    word = input('Enter the word: ')
    word = word.lower()

    if check(word):
        print(vowel(word))
    else:
        print(consonant(word))


main()