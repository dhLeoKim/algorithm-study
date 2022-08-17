import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

d = [0]*(N+1)
for i in range(1, N+1):
    # 점화식
    d[i] = d[i-1] + lst[i-1]

for _ in range(M):
    i, j = map(int, input().split())

    print(d[j] - d[i-1])