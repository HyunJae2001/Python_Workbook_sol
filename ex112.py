def main():
    num_list = []
    avr_list = []

    while True:
        n = input('Enter the number: ')

        if n == '':
            break
        else:
            n = int(n)
            num_list.append(n)
            avr_list.append(sum(num_list) / len(num_list))

    return avr_list


print(main())