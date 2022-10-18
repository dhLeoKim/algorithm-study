import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]

t = 0
while t != T:
    cleaner = []
    dust = []

    # 미세먼지, 공기청정기 위치 정보 받기
    for i in range(R):
        for j in range(C):
            if lst[i][j] == -1:
                cleaner.append([i, j])
            elif lst[i][j] != 0:
                dust.append([i, j])

    # 미세먼지 확산
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    nxt = []
    for i in range(R):
        nxt.append(lst[i][:])
    for i, j in dust:
        A = lst[i][j] // 5
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] != -1 and A:
                nxt[ni][nj] += A
                nxt[i][j] -= A

    # 공기청정기 작동
    up = cleaner[0][0]
    down = cleaner[1][0]
    lst = []
    for i in range(R):
        lst.append(nxt[i][:])
    lst[0] = lst[0][1:] + [nxt[1][C-1]]
    lst[up] = [-1, 0] + lst[up][1:C-1]
    lst[down] = [-1, 0] + lst[down][1:C-1]
    lst[R-1] = lst[R-1][1:] + [nxt[R-2][C-1]]

    for i in range(R):
        if 0 < i < up:
            lst[i][0] = nxt[i-1][0]
            lst[i][C-1] = nxt[i+1][C-1]
        elif down < i < R-1:
            lst[i][0] = nxt[i+1][0]
            lst[i][C-1] = nxt[i-1][C-1]

    t += 1

ret = 0
for row in lst:
    ret += sum(row)

print(ret+2)