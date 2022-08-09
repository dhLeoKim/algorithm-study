N, K = map(int, input().split())
num = list(i for i in input())

for i in range(K):
    num.remove(min(num[0:N-K]))

print(f'{"".join(num)}')