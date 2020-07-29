def return_lyrics(n):
    if n == 1:
        return 'A partridge in a pear tree'
    elif n == 2:
        return 'Two turtle doves'
    elif n == 3:
        return 'Three French hens'
    elif n == 4:
        return 'Four calling birds'
    elif n == 5:
        return 'Five golden ring'
    elif n == 6:
        return 'Six geese a laying'
    elif n == 7:
        return 'Seven swans a swimming'
    elif n == 8:
        return 'Eight maids a milking'
    elif n == 9:
        return 'Nine ladies dancing'
    elif n == 10:
        return 'Ten lords a leaping'
    elif n == 11:
        return 'Eleven pipers piping'
    elif n == 12:
        return 'Twelve drummers drumming'


for i in range(1, 13):
    lyric = return_lyrics(i)
    print(lyric)