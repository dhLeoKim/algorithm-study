# 점화식
# d[i] = d[i-1] + d[i-2] + d[i-3]
# 초기값
# d[1] = 1
# d[2] = 2
# d[3] = 4

T = int(input())
lst = [int(input()) for _ in range(T)]

d = [0]*15

# 초기값
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 14):
    # 점화식
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in lst:
    print(d[i])