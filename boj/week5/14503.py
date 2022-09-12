import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def clean(i, j, d):
    lst[i][j] = 2
    ret = 1
    while True:
        for _ in range(4):
            d = (d-1)%4 
            ni = i + di[d]
            nj = j + dj[d]
            if lst[ni][nj] > 0:
                continue
            i, j = ni, nj
            lst[i][j] = 2
            ret += 1
            break
        else:
            k = (d-2)%4
            ni = i + di[k]
            nj = j + dj[k]
            if lst[ni][nj] == 1:
                return ret
            i, j = ni, nj


N, M = map(int, input().split())
i, j, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

print(clean(i, j, d))