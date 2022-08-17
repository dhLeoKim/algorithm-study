N = int(input())
lst = [int(input()) for _ in range(N)]

# 초기값
d = [0]*(N+1)
d[-1] = {1: 0, 2: 0}
d[0] = {1: lst[0], 2: lst[0]}
# 초기값 d[1] 지정시 indexError
# d[1] = {1: lst[1], 2: d[0][1] + lst[1]}

for i in range(1, N):
    # 점화식
    # d[i] = {1: d[i-2][max(d[i-2], key= lambda x: d[i-2][x])] + lst[i], 2: d[i-1][1] + lst[i]}
    d[i] = {1: max(d[i-2].values()) + lst[i], 2: d[i-1][1] + lst[i]}

print(max(d[N-1].values()))