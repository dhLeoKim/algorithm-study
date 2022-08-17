import sys
input = sys.stdin.readline

N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    # 점화식
    d[i][0] += min(d[i-1][1], d[i-1][2])
    d[i][1] += min(d[i-1][2], d[i-1][0])
    d[i][2] += min(d[i-1][0], d[i-1][1])

print(min(d[N-1]))