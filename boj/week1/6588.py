import sys
import math

def eratos(N):
    check = [False for _ in range(N + 1)]
    for i in range(2, int(math.sqrt(N)) + 1):
        for j in range(i * i, N + 1, i):
            check[j] = True

    return check

check = eratos(1000001)

while True:
    t = int(sys.stdin.readline())
    if t == 0: break

    for i in range(2, t + 1):
        if check[i] != True and check[t - i] != True:
            print(f'{t} = {i} + {t-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")