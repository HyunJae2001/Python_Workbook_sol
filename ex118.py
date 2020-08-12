def createDeck():
    lst = []

    for i in 'shdc':
        for j in range(1, 14):
            if j == 1:
                card = 'A' + i
            elif j == 10:
                card = 'T' + i
            elif j == 11:
                card = 'J' + i
            elif j == 12:
                card = 'Q' + i
            elif j == 13:
                card = 'K' + i
            else:
                card = str(j) + i

            lst.append(card)

    return lst


print(createDeck())