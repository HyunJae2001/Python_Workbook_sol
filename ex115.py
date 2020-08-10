def consonant(word):
    for i in range(len(word)):
        if word[i] in 'aeiou':
            word = word + word[0:i]
            word = word.lstrip(word[0:i])

    return word + 'ay'


def vowel(word):
    return word + 'way'


def check(word):
    if word[0] in 'aeiou':
        return True
    else:
        return False


def main():
    word = input('Enter the word: ')

    if check(word):
        print(vowel(word))
    else:
        print(consonant(word))


main()