import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
d[0][0] = lst[0][0]

# for i in range(min(n, m)):
#     if lst[i][i] == 0: break
#     temp = sum([sum(lst[j][:i+1]) for j in range(i+1)])
#     if temp == (i+1)**2:
#         d[i][i] = temp

N = min(n, m)
for k in range(m-n+1):
    for i in range(k, N):
        if lst[i][i+k] == 0: continue
        temp = sum([sum(lst[j][k:i+k+1]) for j in range(i+1)])
        if temp == (i+1)**2:
            d[i][i+k] = temp
        print(temp)
    print(d)