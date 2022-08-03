# import math

# def bertrand(N):
#     check, prime = [False for _ in range(N + 1)], []
#     for i in range(2, int(math.sqrt(N)) + 1):
#         if check[i] == True: continue
#         prime.append(i)
#         for j in range(i * i, N + 1, i):
#             check[j] = True

#     return check, prime
def bertrand(N):
    cnt = 0
    check = [False for _ in range(2*N + 1)]
    for i in range(2, 2*N + 1):
        if check[i] == True: continue
        if i > N:
            cnt += 1
        for j in range(i * i, 2*N + 1, i):
            check[j] = True

    return cnt

while True:
    n = int(input())
    if n == 0: break

    print(bertrand(n))