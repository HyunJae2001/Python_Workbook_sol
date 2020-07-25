import math
pi = 3
flag = 0

for i in range(2, 15*2+1, 2):
    if flag == 0:
        pi += 4 / (i * (i+1) * (i+2))
        flag = 1
    else:
        pi -= 4 / (i * (i+1) * (i+2))
        flag = 0
    print(pi)