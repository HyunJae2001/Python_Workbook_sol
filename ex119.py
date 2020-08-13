import random


def display(playersDeck, deck):
    for i in range(len(playersDeck)):
        print(f'plaer {i + 1}: {playersDeck[i]}')
    print(f'The remain cards are {deck}')


def deal(player, card, deck):
    playersDeck = []

    for i in range(player):
        playersDeck.append([])

    for i in range(player):
        for j in range(card):
            playersDeck[i].append(deck.pop())

    return playersDeck


def shuffle(lst):
    for i in range(len(lst) ** 2):
        index1, index2 = random.randrange(0, len(lst)), random.randrange(0, len(lst))
        value1, value2 = lst[index1], lst[index2]
        lst[index1], lst[index2] = value2, value1


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


def main():
    player = int(input('Enter the number of players: '))
    card = int(input('Enter the number of cards per player: '))
    deck = createDeck()

    shuffle(deck)
    playersDeck = deal(player, card, deck)

    display(playersDeck, deck)


main()