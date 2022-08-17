# 점화식
# d[i] = min(d[i-1], d[i//2], d[i//3]) + 1
# 초기값
# d[1] = 0

import sys
input = sys.stdin.readline

N = int(input())

p = [0]*1000002
d = [0]*1000002
d[1] = 0

for i in range(2, N+1):
    d[i] = d[i-1] + 1
    p[i] = i-1 

    if i%3 == 0 and d[i] > d[i//3] + 1:
    # if i%3 == 0 and d[i-1] > d[i//3]:
        d[i] = d[i//3] + 1
        p[i] = i//3

    if i%2 == 0 and d[i] > d[i//2] + 1:
    # if i%2 == 0 and d[i-1] > d[i//2]:
        d[i] = d[i//2] + 1
        p[i] = i//2


print(d[N])
print(N, end=' ')
for i in range(d[N]):
    print(p[N], end=' ')
    N = p[N]