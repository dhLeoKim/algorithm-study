M, N = map(int, input().split())

def eratosOfMN(M, N):
    check, prime = [False for _ in range(N + 1)], []
    for i in range(2, N + 1):
        if check[i] == True: continue
        if i >= M:
            prime.append(i)
        for j in range(i * i, N + 1, i):
            check[j] = True

    return prime

for i in eratosOfMN(M, N):
    print(i)