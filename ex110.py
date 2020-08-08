def main():
    int_lst = []

    for i in range(1, 10001):
        div_lst = []

        for j in range(1, (i//2) + 1):
            if i % j == 0:
                div_lst.append(j)

        if sum(div_lst) == i:
            int_lst.append(i)

    return int_lst


print(main())