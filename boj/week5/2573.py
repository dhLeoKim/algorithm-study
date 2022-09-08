import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j):
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        chk[i][j] = True
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        cnt = 0
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and lst[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                if lst[ni][nj] == 0:
                    cnt += 1
        if lst2[i][j] > cnt:
            lst2[i][j] -= cnt
        else:
            lst2[i][j] = 0

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst2 = [row[:] for row in lst]

ice = 0
ret = -1
while True:
    ret += 1
    ice = 0
    chk = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0 and not chk[i][j]:
                BFS(i, j)
                ice += 1

    if ice > 1:
        break

    lst = []
    chk_sum = 0
    for row in lst2:
        lst.append(row[:])
        chk_sum += sum(row)

    if chk_sum == 0:
        ret = 0
        break

print(ret)